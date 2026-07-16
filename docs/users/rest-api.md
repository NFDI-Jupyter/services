# REST API Access

Jupyter4NFDI provides a REST API to programmatically start and stop Jupyter servers. This allows you to integrate JupyterLab into automated workflows, scripts, or external applications.

## Get an API Token

All API endpoints require authentication. You need a JupyterHub API token:

1. Visit [https://hub.nfdi-jupyter.de/hub/token](https://hub.nfdi-jupyter.de/hub/token)
2. Click "Request new API Token" and give it a description
3. Copy the generated token

## Quick Start

### Start a Server

Send a POST request to `/hub/api/start` with user options in JSON format:

```bash
curl -X POST -H "Authorization: token YOUR_TOKEN" https://hub.nfdi-jupyter.de/hub/api/start  
```
    
**Response (200 OK - server running):**
```json
{
  "status": "running",
  "next_url": "https://hub.nfdi-jupyter.de/user/USERNAME/SERVERNAME/",
  "status_url": "https://hub.nfdi-jupyter.de/hub/api/start/USERNAME/SERVERNAME",
  "delete_url": "https://hub.nfdi-jupyter.de/hub/api/users/USERNAME/servers/SERVERNAME"
}
```

**Response (202 Accepted - server starting):**
```json
{
  "status": "pending",
  "status_url": "https://hub.nfdi-jupyter.de/hub/api/start/USERNAME/SERVERNAME",
  "delete_url": "https://hub.nfdi-jupyter.de/hub/api/users/USERNAME/servers/SERVERNAME"
}
```

### Check Server Status

Send a GET request to `/hub/api/start/{username}/{servername}`:

```bash
curl -H "Authorization: token YOUR_TOKEN" https://hub.nfdi-jupyter.de/hub/api/start/USERNAME/SERVERNAME  
```

**Response:**
```json
{
  "status": "running",
  "next_url": "https://hub.nfdi-jupyter.de/user/USERNAME/SERVERNAME/",
  "status_url": "https://hub.nfdi-jupyter.de/hub/api/start/USERNAME/SERVERNAME",
  "delete_url": "https://hub.nfdi-jupyter.de/hub/api/users/USERNAME/servers/SERVERNAME"
}
```

Or if stopped:
```json
{
  "status": "stopped",
  "exit_code": 0,
  "logs": ["..."]
}
```

### Stop a Server

Send a DELETE request to `/hub/api/users/{username}/servers/{servername}`:

```bash
curl -X DELETE -H "Authorization: token YOUR_TOKEN" https://hub.nfdi-jupyter.de/hub/api/users/USERNAME/servers/SERVERNAME  
```

### Stop and delete Server

You may only have 15 Jupyter Server configurations. To delete a Server run the following command:
  
```bash
curl -X DELETE -H "Authorization: token YOUR_TOKEN" -d '{"remove": true}' https://hub.nfdi-jupyter.de/hub/api/users/USERNAME/servers/SERVERNAME
```
  
More details in the official JupyterHub REST API [documentation](https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html#operation/delete-user-server-name)

## User Options

You can customize the server startup using various options:

- **`option`**: Select a version (`default`, `custom`, `repo2docker`).

### Default User Options

The REST API uses the following default options when none are provided:

```python
{
  "option": "custom",
  "custom": {
    "customimage": "jupyter/minimal-notebook:latest",
  },
  "system": "deNBI-Cloud",
  "flavor": "m1",
  "name": "POST API Server",
}
```

### Example with Custom Image

```bash
curl -X POST https://hub.nfdi-jupyter.de/hub/api/start \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "option": "custom",
    "custom": {
      "customimage": "my-custom-image:latest"
    }
  }'
```

### Example with Repo2Docker option

```bash
curl -X POST https://hub.nfdi-jupyter.de/hub/api/start \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "option": "repo2docker",
    "repo2docker": {
      "repotype": "gh",
      "repourl": "binder-examples/requirements",
      "reporef": "HEAD"
    }
  }'
```

## Integration with Jupyter Server API

Once your server is running, you can interact with the underlying Jupyter server using its REST API:

**Documentation**: [Jupyter Server API Documentation](https://jupyter-server.readthedocs.io/en/latest/) | [JupyterLab API Reference](https://jupyterlab.readthedocs.io/en/latest/api/)

### Example: Communicate with Jupyter Server API

```bash
# Get kernel ID
curl -X GET -H "Authorization: token your-token" https://hub.nfdi-jupyter.de/user/USERNAME/SERVERNAME/api
```  

## Error Handling

Common HTTP status codes:

- **200**: Request successful (server running)
- **202**: Request accepted (server starting)
- **403**: Authentication failed
- **404**: Server not found

## Use Cases

- **CI/CD pipelines**: Run automated tests in JupyterLab
- **Batch processing**: Start servers for data processing tasks
- **Custom applications**: Embed JupyterLab in your web application
- **Monitoring tools**: Programmatically manage server lifecycles

## Related Documentation

- [Jupyter4NFDI Website](https://hub.nfdi-jupyter.de)
- [JupyterHub Documentation](https://jupyterhub.readthedocs.io/)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Jupyter Server API](https://jupyter-server.readthedocs.io/en/latest/)
