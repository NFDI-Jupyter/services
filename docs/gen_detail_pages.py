import glob
import os

import mkdocs_gen_files

# get all data
data_dir = "data"
exclude = ["template.yaml", "hooks.py", "cardinfo.yaml", "kernels_and_extensions.yml"]
files = glob.glob(os.path.join(data_dir, "*.yaml"))
services_names = [os.path.splitext(os.path.basename(file_name))[0] for file_name in files]

# generate the pages
for file_name, service_name in zip(files, services_names):
    if os.path.basename(file_name) in exclude:
        continue
    with open(file_name, 'r') as fh:
        d = {"yaml_str": fh.read()}
    target_name = os.path.join("details", service_name + ".md")
    with mkdocs_gen_files.open(target_name, "w") as fh:
        fh.write("---\n")
        fh.write(d["yaml_str"])
        fh.write("---\n")
        #fh.write("{{ macros_info() }}\n\n")
        fh.write("{% include 'details.md' %}\n")
        
    mkdocs_gen_files.set_edit_path(os.path.join("details", service_name +".md"),
                                   "gen_detail_pages.py")


