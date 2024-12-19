# JupyterHub Outpost Architecture

Understanding the JupyterHub Outpost architecture will help you set up and manage Outpost instances effectively, while ensuring your resources remain secure.  
The architecture is divided into two main components: **Local Cluster Components** (associated with the Central JupyterHub) and **Remote Cluster Components** (related to the JupyterHub Outpost installed on a separate cluster from the Central JupyterHub).

## Local Cluster Components

The following key components are part of the central JupyterHub.
> It's recommended to run it on a Kubernetes cluster. Other setups will work as well, but are not covered in this section.

<h3>1. <strong><a href="https://github.com/kreuzert/jupyterhub-outpostspawner">OutpostSpawner</a></strong></h3>

The OutpostSpawner takes on a user's start request for a jupyter server. Instead of starting the server locally, it communicates with a JupyterHub Outpost REST API. It can be used with multiple JupyterHub Outposts, allowing the central JupyterHub to support countless remote systems. For more information look into the OutpostSpawner [documentation](https://jupyterhub-outpostspawner.readthedocs.io/en/latest/).

<h3>2. <strong><a href="https://kubernetes.io/docs/concepts/services-networking/service/">Kubernetes Service</a></strong> (optional) </h3>

Each Jupyter server of a user will receive it's own Kubernetes Service. JupyterHub will be able to communicate with the remote Jupyter server via this local Kubernetes Service, by creating a ssh tunnel to the JupyterHub Outpost.

> If the Jupyter server of a user is reachable from the outside world, e.g. through a Proxy on the remote cluster, it is not required.

## Remote Cluster Components

<h3>1. <strong>JupyterHub Outpost</strong></h3>
The Outpost manages the users Jupyter Servers. It can be configured with any Spawner and has a additional features allowing administrators to be in charge of their own resources. For more information, check the [installation](installation.md) and [configuration](configuration.md) sections.  

> It is recommended to install the JupyterHub Outpost on a Kubernetes cluster using this [Helm Chart](https://artifacthub.io/packages/helm/jupyter-jsc/jupyterhub-outpost). Other setups like docker swarm will work as well, but might require some extra steps.  


## Outpost Setup Scenarios

The diagrams below illustrate various setup configurations with the JupyterHub Outpost. You have the flexibility to add as many systems and Outposts to the architecture as needed.
> Check out the [JupyterHub vanilla architecture](https://jupyterhub.readthedocs.io/en/latest/reference/technical-overview.html#the-major-subsystems-hub-proxy-single-user-notebook-server) for more information about the shown components.

<details>
  <summary>One Remote System
  </summary>
      <p>
        A central JupyterHub initiates Jupyter servers on a remote Kubernetes cluster. 
        The JupyterHub Outpost listens on port 
        <span style="color: #007bff; font-weight: bold;">8080</span> 
        for incoming requests and on port 
        <span style="color: #007bff; font-weight: bold;">22</span> 
        for SSH tunnels, enabling the Jupyter servers (notebooks) to be accessible to the central JupyterHub.
      </p>
  <br><br>
  <div style="display: flex; align-items: flex-start; gap: 20px;">
    <div style="display: flex; justify-content: center; align-items: center; min-width: 45%; max-width: 45%;">
      <img src="../../images/architecture_1.png" alt="Architecture Example with one remote system" style="width: 90%;">
    </div>
    <div style="min-width: 45%; max-width: 45%;">
      <h3>1. <strong>Send Request</strong></h3>
      <p>
      <details><summary>
        The OutpostSpawner handles a user’s request to launch a notebook server. 
      </summary>
        Rather than starting the server itself, it gathers all the necessary details for initiating a single-user server. These typically include the 
        <span style="background-color: #f0f0f0; font-weight: bold;">name</span>, 
        <span style="background-color: #f0f0f0; font-weight: bold;">environment</span>, and 
        <span style="background-color: #f0f0f0; font-weight: bold;">selected user options</span>. 
        Additionally, optional data, such as <span style="background-color: #f0f0f0; font-weight: bold;">certificates</span> 
        or <span style="background-color: #f0f0f0; font-weight: bold;">trust bundles</span> (used for internal SSL), 
        is sent to the <span style="background-color: #f0f0f0; font-weight: bold;">JupyterHub Outpost</span> when required.
      </details>
      </p>
      <h3>2. <strong>Spawner.start()</strong></h3>
      <p>
      <details><summary>
        The JupyterHub Outpost utilizes the configured 
        JupyterHub Spawner to launch the single-user server.
      </summary>
        This process, typically managed directly by <span style="background-color: #f0f0f0; font-weight: bold;">JupyterHub</span>, 
        follows the same sequence of functions used during a standard startup, including 
        <span style="background-color: #f0f0f0; font-weight: bold;">run_pre_spawn_hook</span>, 
        <span style="background-color: #f0f0f0; font-weight: bold;">move_certs</span>, and 
        <span style="background-color: #f0f0f0; font-weight: bold;">start</span>. 
        Any events produced by <span style="background-color: #f0f0f0; font-weight: bold;">_generate_progress()</span> 
        are relayed back to <span style="background-color: #f0f0f0; font-weight: bold;">JupyterHub</span>, ensuring users receive all 
        critical updates without interruption.
      </details>
      </p>
      <h3>3. <strong>Send service address</strong></h3>
      <p>
      <details><summary>
        JupyterHub requires the 
        service address 
        (typically a combination of IP and 
        port) to establish 
        SSH port forwarding.
      </summary>
        This forwarding allows users to access 
        the remote single-user notebook server, even if it is operating within a restricted or isolated environment.
      </details>
      </p>
      <h3>4. <strong>Port forwarding</strong></h3>
      <p>
      <details><summary>
        JupyterHub uses a random available local port (random_port) 
        to forward traffic for the single-user server to the JupyterHub Outpost. 
      </summary>
        It employs 
        <span style="background-color: #f0f0f0; font-weight: bold;">SSH multiplexing</span> to minimize the number of connections. 
        In this setup, the JupyterHub Outpost must have access to the notebook server's 
        <span style="background-color: #f0f0f0; font-weight: bold;">IP address (service_address)</span> 
        and <span style="background-color: #f0f0f0; font-weight: bold;">port (single-user_port)</span>.
        <br>
        Simplified port forward command:
      <pre style="background-color: #f9f9f9; padding: 10px; border-radius: 5px;">
        <code>ssh -L 0.0.0.0:[random_port]:[service_address]:[single-user_port] jhuboutpost@[outpost-ip]</code>
      </pre>
        It is also possible to define a <span style="background-color: #f0f0f0; font-weight: bold;">customized port forwarding function</span> 
        (e.g., to delegate port-forwarding to an external pod, see <em>external tunneling</em>). Alternatively, you can 
        <span style="background-color: #f0f0f0; font-weight: bold;">tunnel directly to the system</span> where the notebook server is running 
        without routing through a JupyterHub Outpost, as described in <em>delayed tunneling</em>.
      </details>
      </p>
      <h3>5. <strong>Create service</strong></h3>
      <p>
      <details><summary>
        At this step, the JupyterHub OutpostSpawner 
        will create a Kubernetes Service, enabling the Configurable HTTP Proxy to communicate with the single-user server via this service.
      </summary>
        <br>
        In the default configuration, the <span style="background-color: #f0f0f0; font-weight: bold;">Hub pod</span> is the target of the Kubernetes service, 
        as it manages the SSH connections. Consequently, all traffic between the client and the single-user server is forwarded through the hub container. 
        <br>
        It is also possible to adjust the <span style="background-color: #f0f0f0; font-weight: bold;">Kubernetes service selector</span> 
        or to define a <span style="background-color: #f0f0f0; font-weight: bold;">customized service creation function</span> 
        (e.g., to delegate port-forwarding to an external pod).
      </details>
      </p>
    </div>
  </div>
</details>



<details>
  <summary>Remote + Local System
  </summary>
    <p>
      This architecture mirrors the one described in the previous section, with the key difference being the addition of a 
      <span style="background-color: #f0f0f0; font-weight: bold;">local JupyterHub Outpost service</span> running on the same 
      <span style="background-color: #f0f0f0; font-weight: bold;">Kubernetes cluster</span> as <span style="background-color: #f0f0f0; font-weight: bold;">JupyterHub</span>. 
      It highlights that, in the case of a local Outpost service, there is no need to enable <span style="background-color: #f0f0f0; font-weight: bold;">SSH port-forwarding</span>, as the 
      <span style="background-color: #f0f0f0; font-weight: bold;">notebook servers</span> will be directly accessible through 
      <span style="background-color: #f0f0f0; font-weight: bold;">Kubernetes’ internal DNS</span> resolution.
    </p>

  <br><br>
  <div style="display: flex; align-items: flex-start; gap: 20px;">
    <div style="display: flex; justify-content: center; align-items: center;">
      <img src="../../images/architecture_2.png" alt="Architecture Example with one remote and one local system" style="width: 70%;">
    </div>
  </div>
</details>


<details>
  <summary>External Tunneling
  </summary>
  <p>
    In this scenario, an additional <span style="background-color: #f0f0f0; font-weight: bold;">pod</span> was created to manage the 
    <span style="background-color: #f0f0f0; font-weight: bold;">port forwarding</span>. This means the management of <span style="background-color: #f0f0f0; font-weight: bold;">SSH tunnels</span> 
    to <span style="background-color: #f0f0f0; font-weight: bold;">single-user notebook servers</span> is delegated from the <span style="background-color: #f0f0f0; font-weight: bold;">JupyterHub pod</span> 
    to the external <span style="background-color: #f0f0f0; font-weight: bold;">port forwarding pod</span>.
  </p>
  <p>
    With this setup, <span style="background-color: #f0f0f0; font-weight: bold;">single-user servers</span> remain reachable even if 
    <span style="background-color: #f0f0f0; font-weight: bold;">JupyterHub</span> itself is offline. Instead of tunneling through the 
    <span style="background-color: #f0f0f0; font-weight: bold;">Hub pod</span>, traffic between the client and the single-user server 
    travels through the <span style="background-color: #f0f0f0; font-weight: bold;">port forwarding pod</span>. The <span style="background-color: #f0f0f0; font-weight: bold;">Kubernetes service</span> 
    for the single-user server is then configured to target the <span style="background-color: #f0f0f0; font-weight: bold;">port forwarding pod</span> 
    rather than the <span style="background-color: #f0f0f0; font-weight: bold;">Hub pod</span>.
  </p>
  <div style="display: flex; align-items: flex-start; gap: 20px;">
    <div style="display: flex; justify-content: center; align-items: center;">
      <img src="../../images/architecture_3.png" alt="Architecture Example with external tunneling" style="width: 70%;">
    </div>
  </div>
</details>

<details>
  <summary>Delayed Tunneling
  </summary>
  <p>
    In this scenario, an additional <span style="background-color: #f0f0f0; font-weight: bold;">pod</span> was created to manage the 
    <span style="background-color: #f0f0f0; font-weight: bold;">port forwarding</span>. This means the management of <span style="background-color: #f0f0f0; font-weight: bold;">SSH tunnels</span> 
    to <span style="background-color: #f0f0f0; font-weight: bold;">single-user notebook servers</span> is delegated from the <span style="background-color: #f0f0f0; font-weight: bold;">JupyterHub pod</span> 
    to the external <span style="background-color: #f0f0f0; font-weight: bold;">port forwarding pod</span>.
  </p>
  <p>
    With this setup, <span style="background-color: #f0f0f0; font-weight: bold;">single-user servers</span> remain reachable even if 
    <span style="background-color: #f0f0f0; font-weight: bold;">JupyterHub</span> itself is offline. Instead of tunneling through the 
    <span style="background-color: #f0f0f0; font-weight: bold;">Hub pod</span>, traffic between the client and the single-user server 
    travels through the <span style="background-color: #f0f0f0; font-weight: bold;">port forwarding pod</span>. The <span style="background-color: #f0f0f0; font-weight: bold;">Kubernetes service</span> 
    for the single-user server is then configured to target the <span style="background-color: #f0f0f0; font-weight: bold;">port forwarding pod</span> 
    rather than the <span style="background-color: #f0f0f0; font-weight: bold;">Hub pod</span>.
  </p>
  <div style="display: flex; align-items: flex-start; gap: 20px;">
    <div style="display: flex; justify-content: center; align-items: center;">
      <img src="../../images/architecture_4.png" alt="Architecture Example with external tunneling" style="width: 70%;">
    </div>
  </div>
</details>