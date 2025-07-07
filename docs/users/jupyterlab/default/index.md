# JupyterLab

## Systems Available

**JupyterLab** default version is available on these systems:

- **deNBI-Cloud**
- **JSC-Cloud**

> Files in `/home/jovyan` are stored persistently. Everything else will be lost after a restart.

## Environment
The default environment for JupyterLab is based on the official [jupyter/minimal-notebook](https://github.com/jupyter/docker-stacks/tree/main/images/minimal-notebook).  

## Kernel customization
> To use your own environment and packages it is recommended to use the [Repo2Docker](../repo2docker/index.md) option, as this provides way more options and is easier to use.  
To install a new kernel in your running JupyterLab simply run:  
```
python -m ipykernel install --user --name mykernel --display-name "MyKernel"
```

This will create a kernelspec file at `/home/jovyan/.local/share/jupyter/kernels/mykernel/kernel.json`. You can update this, to use any environment you like to use.  

### Use own virtualenv
```
1. python3 -m venv /home/jovyan/.local/share/jupyter/kernels/venv_mykernel
2. /home/jovyan/.local/share/jupyter/kernels/venv_mykernel/bin/pip install ipykernel  # ipykernel is required in each environment
3. # Replace "/opt/conda/bin/python" in /home/jovyan/.local/share/jupyter/kernels/mykernel/kernel.json with "/home/jovyan/.local/share/jupyter/kernels/venv_mykernel/bin/python"
4. Using "MyKernel" will then use the newly created python environment
```
