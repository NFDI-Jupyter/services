import glob
import logging
import os
import requests
import yaml

exclude = ["template.yaml", "hooks.py", "cardinfo.yaml"]

def _get_data():
    # get all data
    data_dir = "data"
    files = glob.glob(os.path.join(data_dir, "*.yaml"))
    services_names = [os.path.splitext(os.path.basename(file_name))[0] for file_name in files]
    return files, services_names

def generate_cards(*args, **kwargs):
    files, services_names = _get_data()
    # generate the pages
    with open("data/cardinfo.yaml", "w") as outfile:
        for file_name, service_name in zip(files, services_names):
            if os.path.basename(file_name) in exclude:
                continue
            with open(file_name, 'r') as fh:
                d = yaml.safe_load(fh)
                logo = d.get("logo", None)
                if logo is None:
                    if os.path.exists("docs/assets/"+ file_name.split("/")[-1][:-4]+"png"):
                        logo = file_name.split("/")[-1][:-4]+"png"
                    else:
                        logo = "default-logo.png"
                url_requires = d.get("service_url_requirement", False)
                if url_requires:
                    service_url = "#"
                    button_attr = ".md-button--disabled"
                else:
                    service_url = d["service_url"]
                    button_attr = ".md-button .md-button--primary"
                lock = ":material-lock:" if d.get("restricted", True) else ":material-lock-open-variant:"

                outfile.write("- title: %s\n" % d["title"])
                outfile.write("""  content: |
    Provider: *%s*
    <p class=\"nt-card-text\">Target Group: %s</p>\n
    <div class=\"nfdi-card-link\">[:octicons-arrow-right-24: Service Details](details/%s.md)\n
    [%s Login](%s){%s}</div>\n""" % (d["provider"],
                                     d["target_group_open_for"],
                                     service_name,
                                     lock,
                                     service_url,
                                     button_attr))
                outfile.write("  image: assets/%s\n" % logo)
                outfile.write("  icon: \":octicons-arrow-right-24:\"\n")


def _get_lat_lon(city_name):
    """ Get latitude and longitude for a city"""
    api_url = f"https://nominatim.openstreetmap.org/search?format=json&q={city_name}"
    response = requests.get(api_url)
    data = response.json()

    if data:
        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])
        return latitude, longitude
    else:
        return None, None


def generate_svg(*args, **kwargs):
    # SVG Dimensions
    SVG_WIDTH = 1000
    SVG_HEIGHT = 1360

    # Geographic Bounds of Germany
    MIN_LATITUDE = 47.28   # Southernmost Point
    MAX_LATITUDE = 55.06   # Northernmost Point
    MIN_LONGITUDE = 6.19  # Westernmost Point
    MAX_LONGITUDE = 14.66  # Easternmost Point

    # Calculate Scaling Factors
    latitude_scaling_factor = SVG_HEIGHT / (MAX_LATITUDE - MIN_LATITUDE)
    longitude_scaling_factor = SVG_WIDTH / (MAX_LONGITUDE - MIN_LONGITUDE)

    files, services = _get_data()
    with open("docs/assets/germany-map.svg", "r") as svg_file:
        svg_content = svg_file.read()

    for file_name, service_name in zip(files, services):
        if os.path.basename(file_name) in exclude:
            continue
        with open(file_name, 'r') as fh:
            d = yaml.safe_load(fh)
        city = d.get("provider_location", None)
        latitude = longitude = None
        if city is None:
            logging.warning(f'*City* of {service_name} is not given. It cannot be included in the map')
        else:
            latitude, longitude = _get_lat_lon(city)
        if latitude is None or longitude is None:
            logging.warning(f"City not found: {city}")
        else:
            # Convert Specific Geographic Coordinates to SVG Coordinates
            svg_x = (longitude - MIN_LONGITUDE) * longitude_scaling_factor
            svg_y = SVG_HEIGHT - (latitude - MIN_LATITUDE) * latitude_scaling_factor
            #print(f"SVG Coordinates for {city}: X={svg_x}, Y={svg_y}")
            # Define the circle element as a string
            circle_element = f'<circle cx="{svg_x}" cy="{svg_y}" r="5" fill="red" />'
            # Find the position to insert the circle element
            insert_position = svg_content.find('</g>')
            # Insert the circle element into the SVG content
            if insert_position != -1:
                svg_content = svg_content[:insert_position] + circle_element + svg_content[insert_position:]

    with open("docs/assets/germany-map.svg", "w") as svg_file:
        svg_file.write(svg_content)


def generate(*args, **kwargs):
    """Wrapper function for simple hooks plugin (only accepts one function) """
    generate_cards(args, kwargs)
    generate_svg(args, kwargs)