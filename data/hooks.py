import glob
import os
import yaml

def generate_cards(*args, **kwargs):

    # get all data
    data_dir = "data"
    exclude = ["template.yaml","hooks.py","cardinfo.yaml", "kernels_and_extensions.yml"]
    files = glob.glob(os.path.join(data_dir, "*.yaml"))
    services_names = [os.path.splitext(os.path.basename(file_name))[0] for file_name in files]

    # generate the pages
    with open ("data/cardinfo.yaml", "w") as outfile:
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
