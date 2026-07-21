#!/bin/bash

# Author: Katharina Höflich
# Repository: https://github.com/FZJ-JSC/jupyter-jsc-notebooks

SINGULARITY_IMAGE=/p/project/cesmtst/hoeflich1/jupyter-base-notebook/jupyter-base-notebook.sif
JUPYTERJSC_USER_CMD="singularity exec ${SINGULARITY_IMAGE} jupyterhub-singleuser --config ${JUPYTER_LOG_DIR}/config.py"
