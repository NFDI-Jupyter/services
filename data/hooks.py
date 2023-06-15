import glob
import os
import yaml

def generate_cards(*args, **kwargs):

    # get all data
    data_dir = "data"
    exclude = ["template.yaml","hooks.py","cardinfo.yaml"]
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
                    
                outfile.write("- title: %s\n"%d["title"])
                outfile.write("""  content: |
    Provider: *%s*\n
    <div class=\"nfdi-card-link\">[:octicons-arrow-right-24: Service Details](details/%s/)\n
    [:material-lock: Login](%s){.md-button .md-button--primary}</div>\n"""%(d["provider"],service_name, d["service_url"]))
                outfile.write("  image: assets/%s\n" % logo)
                outfile.write("  icon: \":octicons-arrow-right-24:\"\n")
