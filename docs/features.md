# Available Resources and Tools

Jupyter4NFDI provides a variety of options and features to enhance your interactive computing experience. Here’s an overview of what you can expect:

## 1. Systems Available

### Cloud

**deNBI-Cloud** is accessible to everyone, providing flexible cloud resources. For users utilizing JSC-Cloud, we offer several resource configurations, including:

- **2GB RAM, 1 CPU** for **2 hours** (mostly used for Repo2Docker shared sessions)
- **2GB RAM, 1 CPU** for **5 days**
- **4GB RAM, 1 CPU** for **2 days**
- **8GB RAM, 2 CPUs** for **10 hours**

**JSC-Cloud** is accessible to everyone, providing flexible cloud resources. For users utilizing JSC-Cloud, we offer several resource configurations, including:

- **2GB RAM, 1 CPU** for **7 days**
- **4GB RAM, 1 CPU** for **2 days**
- **8GB RAM, 2 CPUs** for **10 hours**

Please note that these flavors may change in the future and are dependent on the available resources.

With **deNBI-Cloud** and **JSC-Cloud**, each user enjoys **25GB** of **persistent storage**, allowing you to keep your important work safe and accessible. This feature is available not only in the **default JupyterLab versions** but also when using **custom Docker images** or **Repo2Docker**. Whether you're developing in a standard environment or tailoring your setup with your own images, you can rest assured that your data is securely stored and easily retrievable.

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

