#!/bin/bash

# Author: Katharina Höflich
# Repository: https://github.com/FZJ-JSC/jupyter-jsc-notebooks

KERNEL_NAME=${1}
SINGULARITY_IMAGE=${2}

[[ ! -z "$KERNEL_NAME" ]] || echo "Provide a Jupyter kernel name, please."
[[ ! -z "$SINGULARITY_IMAGE" ]] || echo "Provide a Singularity container image, please."

USER_KERNEL_DIR=${HOME}/.local/share/jupyter/kernels/${KERNEL_NAME}
mkdir -p ${USER_KERNEL_DIR} || exit

#
#echo '{
# "argv": [
#  "'"${USER_KERNEL_DIR}"'/singularity-kernel.sh",
#  "-f",
#  "{connection_file}"
# ],
# "display_name": "'"${KERNEL_NAME}"'",
# "language": "python"
#}' > ${USER_KERNEL_DIR}/kernel.json || exit
#
#echo '#!/bin/bash
#module purge
#SINGULARITY_IMAGE='"${SINGULARITY_IMAGE}"'
#singularity run ${SINGULARITY_IMAGE} python -m ipykernel $@
#' > ${USER_KERNEL_DIR}/singularity-kernel.sh || exit
#
#chmod +x ${USER_KERNEL_DIR}/singularity-kernel.sh
#

echo '{
 "argv": [
   "singularity",
   "exec",
   "--cleanenv",
   "'"${SINGULARITY_IMAGE}"'",
   "python",
   "-m",
   "ipykernel",
   "-f",
   "{connection_file}"
 ],
 "language": "python",
 "display_name": "'"${KERNEL_NAME}"'"
}' > ${USER_KERNEL_DIR}/kernel.json || exit
