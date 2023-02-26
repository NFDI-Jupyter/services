
# Join the list

To become part of the list of JupyterHub instances of Germany you have to provide a yaml-file with the information listed in the table below. You can check out existing yaml-files and a template you can base on in the `data` folder. You can also add a logo of your service is the `assets` folder. When everything is ready, please add a pull request to the main branch of this repository. If you need further assistance or have other questions, do not hesitate to open an issue.


| YAML&nbsp;Key&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Required? | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Example |
|----------|-----------|-------------------------|-------------------------|
| `title`     | yes       | The service name. If too general, should include a provider or project context. | NFDI4Ing JupyterHub |
| `provider` | yes       | All service providers.   | University of Stuttgart, Technical University of Darmstadt |
| `service_url`      | yes       | Link address to the entrypoint for users. | https://jupyter.nfdi4ing.de |
| `support` | yes | Where to get help | fokus@izus.uni-stuttgart.de |
| `health api_url` | no        | Healthcheck URL | green / orange / red
| `documentation_url` | no | Link address to service specific documentation | |
| `target_group_open_for` | yes | Roles, domain, NFDI consortia, University, etc. | Researchers of NFDI4Ing |
| `login_process` |  yes | How is the login performed; Login-URL | Login via DFN-AAI & eduGAIN |
| `features` | yes | What the services offers | |
| -- `version` | yes | 1.x or 2.x version of Juyterhub?; classic notebook or lab view? | 1.x JupyterHub (classic view)
| -- `kernels` | no | List of provided kernels. | Python, Julia, R |
| -- `extensions` | no | List of provided server-side / client-side JupyterHub extensions | |
| -- `proxy_apps` | no | List of server-proxy featured applications. | MATLAB IDE |
| -- `install` | yes | Whether it is allowed to install further packages, kernels, extensions | yes |
| -- `shared_folde`r | yes | Whether there is a folder to share documents with others | false |
| -- `persistent_storage` | yes | Whether documents can survice the docker session. | true |
| -- `misc` | no | List of other features you find relevant, e.g. dynamic image creation | | 
| `resources` | yes | Information about available resources on the instance | |
| -- `default_server_user` | no | Default number of Jupyter servers per user | 1 |
| -- `max_server_user` | yes | Maximum number of Jupyter servers per user | 5 |
| -- `default_cpu` | no | Default number of CPU for a Jupyter server | 1 |
| -- `max_cpu` | yes | Maximum number of CPU for a Jupyter server | 4 |
| -- `default_cpu_time` | no | Default CPU time for a Jupyter server | 1 h |
| -- `max_cpu_time` | yes | Maximum CPU time for a Jupyter server | 72 h |
| -- `default_memory` | no | Default amount of memory for a Jupyter server | 100 MB |
| -- `max_memory` | yes | Maximum amount of memory for a Jupyter server | 4 GB |
| -- `default_gpu` | no | Default number of GPU for a Jupyter server | 0 |
| -- `max_gpu` | yes | Maximum number of GPU for a Jupyter server | 0 |
| -- `default_disk` | no | Default amount of disk space (maybe temporary) for a Jupyter server | 10 GB |
| -- `max_disk` | yes | Maximum amount of disk space (maybe temporary) for a Jupyter server | 10 GB |
| -- `default_persistent_disk` | no | Default amount of disk space that services a Jupyter session | 2 GB |
| -- `max_persistent_disk` | yes | Maximum amount of disk space that services a Jupyter session | 2 GB |

