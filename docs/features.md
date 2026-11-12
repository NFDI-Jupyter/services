# Available Resources and Tools

Jupyter4NFDI provides a variety of options and features to enhance your interactive computing experience. Here’s an overview of what you can expect:

## 1. Systems Available

> The amount of credits you receive depends on the information we get from the AAI. Using GitHub / Google / Orcid may lead to a reduced amount of credits.

### Cloud

**deNBI-Cloud** and **JSC-Cloud** are accessible to everyone, providing flexible cloud resources. On both systems, we offer the following resource configurations:

- **2GB RAM, 1 CPU** for **10 credits per hour**
- **4GB RAM, 1 CPU** for **20 credits per hour**
- **8GB RAM, 4 CPUs** for **40 credits per hour**
- **16GB RAM, 4 CPUs** for **80 credits per hour**

> **Need more power for your session?** Both **deNBI-Cloud** and **JSC-Cloud** can give you **GPU-enabled sessions** as well as **flavors with more memory** than the ones listed above. Since these resources are limited, they are **not enabled by default** — but getting them is just a short message away: simply [contact support](support.md), tell us why you need it, and we will unlock the corresponding flavors for your account. All the details, including the available GPU profiles and the request process, can be found on the [GPU Access](users/gpu-access.md) page.

Please note that these flavors may change in the future and are dependent on the available resources.

With **deNBI-Cloud** and **JSC-Cloud**, each user enjoys **25GB** of **persistent storage**, allowing you to keep your important work safe and accessible. This feature is available not only in the **default JupyterLab versions** but also when using **custom Docker images** or **Repo2Docker**. Whether you're developing in a standard environment or tailoring your setup with your own images, you can rest assured that your data is securely stored and easily retrievable.

**The GWDG Cloud** is a third system available through Jupyter4NFDI, operated by the [GWDG](https://www.gwdg.de).

The GWDG Jupyter-Cloud provides a **default flavor** with **2 CPU and 8 GB of RAM**. Sessions can run for up to **24 hours**.

> We will add more systems to Jupyter4NFDI in the future.

## 2. Different JupyterLab Versions

Jupyter4NFDI supports multiple versions of **JupyterLab**, allowing users to select the environment that best suits their needs. This flexibility ensures compatibility with various extensions and workflows.

Currently available JupyterLab versions:

 - **JupyterLab** - A default setup based on the official [jupyter/minimal-notebook](https://github.com/jupyter/docker-stacks/tree/main/images/minimal-notebook) image.
 - **JupyterLab XL** - A JupyterLab setup with multiple pre-installed kernels and environments. 
 - **Custom Docker Image** - Use your own docker image. More details in [Custom Docker Images](users/jupyterlab/customdockerimage/index.md).
> The mount path for your persistent storage is configurable. This flexibility ensures that the storage location does not interfere with the specific requirements of the Docker image you provide. You can easily adapt the mounting path to suit your environment, allowing for a seamless integration of your custom setup.
 - **Repo2Docker ( Binder )** - Build docker images directly from GitHub, GitLab, Zenodo or other sources. More details in [Repo2docker Integration](users/jupyterlab/repo2docker/index.md).


---

Explore these options to make the most out of your experience with Jupyter4NFDI, whether you are conducting research, teaching, or learning!

