# GPU Access

Jupyter4NFDI now offers GPU-enabled resources for compute-intensive tasks such as machine learning, deep learning, and scientific computing. However, GPU resources are currently limited and require special access.

## GPU Availability

Currently, GPU access is available on a limited number of GPU-enabled nodes. These resources are shared among all users and allocated on a first-come, first-served basis.

### Available GPU Profiles

When GPU access is enabled for your account, you may select from the following GPU profiles:

- **JSC-Cloud**: 1 GPU (Nvidia A100 80GB PCIe), 8GB RAM, 2 VCPU
- **deNBI-Cloud**: 1 GPU (Nvidia Tesla V100 PCIE 16GB), 8GB RAM, 2 VCPU

On JSC-Cloud the we're using the [Nvidia Multi Instance GPU](https://www.nvidia.com/en-gb/technologies/multi-instance-gpu/) feature. On deNBI-Cloud we're using a time-sliced approach, since MIG is not supported for the V100 GPU.

## How to Request GPU Access

Due to the limited availability of GPU resources, access must be requested individually. To request GPU access:

1. **Contact us via email** at `jupyter4nfdi at lists.nfdi.de`
2. Include the following information in your request:
   - Purpose of GPU usage (e.g., machine learning, deep learning, specific research project)
   - Expected duration of GPU usage
   - Any specific requirements or questions

### Approval Process

After submitting your request, our team will review it and typically respond within 1-2 business days. Once approved, you'll receive an email invitation from Helmholtz ID to a virtual organization. Joining this virtual organization will grant you access to the GPU flavors.

## Support

For questions about GPU access or to request access:

- **Email**: `jupyter4nfdi at lists.nfdi.de`
- **Technical Support**: `ds-support at fz-juelich.de`
- **Chat**: [NFDI Mattermost](https://all-chat.nfdi.de) (Channel `#jupyter4nfdi`)

## Future Plans

We are actively working on expanding GPU availability to all users without requiring individual access requests. This includes:

- Adding more GPU nodes to our infrastructure
- Implementing automated access control and resource management
- Improving GPU resource scheduling and allocation

Our goal is to make GPU resources readily available for all users who need them for their research and projects.
