# Available Resources and Tools

Jupyter4NFDI provides a variety of options and features to enhance your interactive computing experience. Here’s an overview of what you can expect:

## 1. Systems Available

### Cloud

**JSC-Cloud** is accessible to everyone, providing flexible cloud resources. For users utilizing JSC-Cloud, we offer several resource configurations, including:

- **2GB RAM, 1 CPU** for **7 days**
- **4GB RAM, 1 CPU** for **2 days**
- **8GB RAM, 2 CPUs** for **10 hours**

Please note that these flavors may change in the future and are dependent on the available resources.

With JSC-Cloud, each user enjoys **25GB** of **persistent storage**, allowing you to keep your important work safe and accessible. This feature is available not only in the **default JupyterLab versions** but also when using **custom Docker images**. Whether you're developing in a standard environment or tailoring your setup with your own images, you can rest assured that your data is securely stored and easily retrievable.

> We will add more systems to Jupyter4NFDI in the future. 

## 2. Different JupyterLab Versions

Jupyter4NFDI supports multiple versions of **JupyterLab**, allowing users to select the environment that best suits their needs. This flexibility ensures compatibility with various extensions and workflows.

Currently available JupyterLab versions:

 - **JupyterLab 4.2** - A default setup of useful kernels, extensions and more. More details [here](https://github.com/easybuilders/JSC/blob/2024/Golden_Repo/j/Jupyter-bundle/Jupyter-bundle-20240520-GCCcore-12.3.0.eb).
> your persistent storage is mounted to `/home/jovyan`. Everything outside of this directory will be lost after a restart.
 - **JupyterLab 3.6** - the previous default version. No longer actively supported. More details [here](https://github.com/easybuilders/JSC/blob/2023/Golden_Repo/j/JupyterLabCollection/JupyterLabCollection-2023.3.6-GCCcore-11.3.0.eb).
> your persistent storage is mounted to `/home/jovyan`. Everything outside of this directory will be lost after a restart.
 - **Custom Docker Image** - Use your own docker image. More details in [Custom Docker Images](users/jupyterlab/customdockerimage/index.md).
> The mount path for your persistent storage is configurable. This flexibility ensures that the storage location does not interfere with the specific requirements of the Docker image you provide. You can easily adapt the mounting path to suit your environment, allowing for a seamless integration of your custom setup.
 - **Repo2Docker ( Binder )** - Build docker images directly from GitHub, GitLab, Zenodo or other sources. More details in [Repo2docker Integration](users/jupyterlab/repo2docker/index.md).


---

Explore these options to make the most out of your experience with Jupyter4NFDI, whether you are conducting research, teaching, or learning!

