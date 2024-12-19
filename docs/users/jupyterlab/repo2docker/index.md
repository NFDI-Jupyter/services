# Repo2Docker ( Binder )

Jupyter4NFDI offers **Repo2Docker ( Binder )**, which facilitates building Docker images directly from GitHub, GitLab, Zenodo or other sources. This capability allows users to easily set up environments that replicate their local development setups or share projects with others. Combined with the **[share](../../misc.md#share-button)** Button, it allows you easily to create FAIR digital objects.

> This service is currently in a beta stadium. We will continue working on it to bring more features and improvements.

## Systems Available

**Repo2Docker ( Binder )** is available on these systems:

- **JSC-Cloud**

## Options

<div style="text-align: center;">
  <img src="../../../images/repo2docker.png" alt="CustomDockerImages" style="width: 90%;">
</div>

### Repository Type

- **Description:** Select the type of repository where your project is hosted. Currently only GitHub is supported. Other options will be added in the future:
  - **GitHub:** The most common choice for code repositories.
- **Purpose:** This determines how Repo2Docker connects to and retrieves your repository content.

### URL

- **Description:** Enter the full URL of your repository. For GitHub, this is typically in the format `https://github.com/username/repository-name`.
- **Purpose:** This is the source that Repo2Docker will use to build your containerized environment. Make sure the URL is accessible and public or configured for access.

### Git Ref

- **Description:** Specify a reference for the desired version of your repository.
  - **Branch name:** e.g., `main`, `dev`
  - **Tag:** Use release tags, such as `v1.0`
  - **Commit hash:** Input a specific commit ID, useful for precise versions
  - **Custom references:** Use `HEAD~n` or `@~n` to go back `n` commits from the latest commit.
- **Purpose:** Allows you to control exactly which version of the repository is used, ensuring reproducibility.

### Path to a Notebook File or URL

- **Description:** Optionally, provide the path to a specific notebook file within your repository, e.g. `notebooks/example.ipynb`, or a URL, e.g. `voila`/`doc/tree/example.ipynb`, to open.
- **Purpose:** If filled, the specified notebook will open automatically once the environment is launched, simplifying access to a main file.

## Persistence and Shared Environments

Changes made within the running JupyterLab environment are **not persistent**. This means:

- **Non-Persistent** Changes: Any modifications made to files or settings in the current JupyterLab session will be lost when the session is closed. They are only visible to the current user session and will not persist across restarts.
- **No Shared State**: If you share a link to your environment, other users who start a JupyterLab session from that link will see the repository's original content, not any changes you’ve made in your session.
- **No Persistent Storage**: The current Repo2Docker setup does not support persistent storage. If you need to save your work, download any necessary files before closing the session.

> In the future, we plan to add persistent storage, allowing you to mount **your persistent data** directly into the session when it starts.