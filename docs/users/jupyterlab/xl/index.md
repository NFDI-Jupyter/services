# JupyterLab XL

This is the current default version of JupyterLab on Jupyter4NFDI. In the next sections we will describe how you can modify it to fit your needs, and give a brief overview of the installed software. It may be updated in the future to keep software up to date.

> Last Update of JupyterLab XL on 21.07.2026

## Systems Available

**JupyterLab XL** is available on these systems:

- **JSC-Cloud**

> On **JSC-Cloud** only files in `/home/jovyan` are stored persistently. Everything else will be lost after a restart.

## Pre-installed kernels
> The kernels listed in this documentation may not always be up-to-date, as they can change periodically. For the current list of available kernels, please check the web service. The configuration files used to install these kernels are stored [here in our GitHub repository](https://github.com/easybuilders/JSC/tree/2026/Golden_Repo/j).

- [Bash](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterKernel-Bash/JupyterKernel-Bash-0.10.0-GCCcore-14.3.0-4.5.5.eb)
- [Cling](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterKernel-Cling/JupyterKernel-Cling-1.2-GCCcore-14.3.0-4.5.5.eb)
- [Java](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterKernel-Java/JupyterKernel-Java-3.0.2-GCCcore-14.3.0.eb)
- [Julia](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterKernel-Julia/JupyterKernel-Julia-1.12.3-GCCcore-14.3.0.eb)
- [LFortran](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterKernel-LFortran/JupyterKernel-LFortran-0.61.0-GCCcore-14.3.0.eb)
- [Octave](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterKernel-Octave/JupyterKernel-Octave-11.1.0-GCCcore-14.3.0-4.5.5.eb)
- [R](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterKernel-R/JupyterKernel-R-4.5.2-GCCcore-14.3.0-4.5.5.eb)
- [Ruby](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterKernel-Ruby/JupyterKernel-Ruby-3.4.7-GCCcore-14.3.0.eb)

You can select them by navigating to the **Kernels and Extensions** tab on the left side of your configuration.

<div style="text-align: center;">
  <img src="../../../images/kernels_and_extensions.png" alt="Kernels" style="width: 70%;">
</div>

## Kernel customization

> It might be easier to create your own environment using [Repo2Docker](../repo2docker/index.md).  
  
> Since JupyterLab 4.3 uses software loaded via lmod, one cannot simply install a kernel without loading these modules first. Please follow the steps in the these guides to create your own kernel.  

> Having trouble setting up kernels? Check the logs at `/tmp/custom/logs/stdout` in your JupyterLab.

- [Create kernel with virtualenv](kernels_venv.ipynb)


## Extensions
> The extensions listed in this documentation may not always be up-to-date, as they can change periodically. For the current list of available extensions, please check the web service. The configuration files used to install these extensions are stored [here in our GitHub repository](https://github.com/easybuilders/JSC/tree/2026/Golden_Repo/j).

- [Jupyter Archive](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyter-archive/jupyter-archive-3.4.0-GCCcore-14.3.0.eb)
- [Jupyter Bokeh](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyter-bokeh/jupyter-bokeh-4.0.5-GCCcore-14.3.0.eb)
- [Jupyter Collaboration](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyter-collaboration/jupyter-collaboration-4.2.1-GCCcore-14.3.0.eb)
- [Jupyter Resource Usage](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyter-resource-usage/jupyter-resource-usage-1.2.0-GCCcore-14.3.0.eb)
- [Jupyter Server Proxy](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyter-server-proxy/jupyter-server-proxy-20260302-GCCcore-14.3.0.eb)
- [JupyterLab Code Formatter](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-code-formatter/jupyterlab-code-formatter-3.0.3-GCCcore-14.3.0.eb)
- [JupyterLab DataMount](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-data-mount/jupyterlab-data-mount-1.1.0-GCCcore-14.3.0.eb)
- [JupyterLab favorites](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-favorites/jupyterlab-favorites-3.5.0-GCCcore-14.3.0.eb)
- [JupyterLab Git](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-git/jupyterlab-git-0.52.0-GCCcore-14.3.0.eb)
- [JupyterLab GitLab](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-gitlab/jupyterlab-gitlab-4.0.0-GCCcore-14.3.0.eb)
- [JupyterLab H5Web](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-h5web/jupyterlab-h5web-12.6.1-GCCcore-14.3.0.eb)
- [JupyterLab Hub Credit Extension](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-hub-credit-extension/jupyterlab-hub-credit-extension-0.2.1-GCCcore-14.3.0.eb)
- [JupyterLab LaTeX](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-latex/jupyterlab-latex-4.4.0-GCCcore-14.3.0.eb)
- [JupyterLab lsp](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-lsp/jupyterlab-lsp-5.2.0-GCCcore-14.3.0.eb)
- [JupyterLab VariableInspector](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterlab-variableinspector/jupyterlab-variableinspector-3.2.4-GCCcore-14.3.0.eb)
- [JupyterView](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/jupyterview/jupyterview-0.8.0-GCCcore-14.3.0.eb)

> Most extensions are always loaded. Others can be activated to your liking in the **Kernels and Extensions** tab in your JupyterLab configuration.


## Proxies

- [RStudio](https://github.com/easybuilders/JSC/blob/2026/Golden_Repo/j/JupyterProxy-RStudio/JupyterProxy-RStudio-2025.12.0-GCCcore-14.3.0.eb)
