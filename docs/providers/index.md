# JupyterHub Outpost for Jupyter4NFDI

Welcome to the JupyterHub Outpost installation guide for external resource providers! This guide will help you set up a JupyterHub Outpost on your resources, allowing users within the Jupyter4NFDI community to benefit from access to diverse computational environments while you maintain control over your resources.

## Why Join Jupyter4NFDI?

Jupyter4NFDI brings together resources from multiple providers to create a rich and collaborative environment, promoting knowledge sharing and enabling cutting-edge research. Here’s why you should consider contributing:

- **Security and Control**: You control who may access your resources. Permissions and access rights remain fully in your hands.
- **Visibility**: By connecting your resources to Jupyter4NFDI, you increase their visibility and attract a wider range of users within the scientific community.
- **Collaborative Community**: Join a network of peers contributing to NFDI's vision of federated, accessible research infrastructure.
- **Complementary Service**: JupyterHub Outpost doesn't replace or compromise any existing JupyterHub instances you may be running. Instead, it provides an additional access point specifically configured for NFDI needs.

JupyterHub Outpost is a powerful, flexible solution that works in tandem with your existing systems. The following sections will guide you through its architecture, installation, and configuration.

## Features

- Use a central JupyterHub to offer jupyter servers on multiple systems of potentially different types.
- User specific flavors allows administrators to configure resource limits for each user.
- Each (remote) system may use a different JupyterHub Spawner.
- Forward spawn events gathered by the remote Spawner to the user.
- Users may override the configuration of the remote Spawner at runtime (e.g. to select a different Docker Image), if allowed by JupyterHub Outpost administrators.
- Integrated SSH port forwarding solution to reach otherwise isolated remote jupyter servers.
- Supports the JupyterHub internal_ssl feature.
- One JupyterHub Outpost can be connected to multiple JupyterHubs without the Hubs interfering with each other.
- Configuration of JupyterHub Outpost similar to the JupyterHub configuration.
