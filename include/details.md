icon: fontawesome/solid/info
# {{ title }}
The {{ title }} can be reached [here]({{ service_url }}) and is provided by {{ provider }}.

## Short Facts
__Service URL__

: [{{ service_url }}]({{ service_url }})

__Target group__

: {{ target_group_open_for }}

__Login process__

: {{ login_process }} 

__Support__

: {{ support|urlize }}

__Documentation__

: {% if documentation_url %}[{{ documentation_url }}]({{ documentation_url }}){% else %}None{% endif %}



## Features 
{{ title }} offers:

=== "General"

    - Version(s): {{ features.version }}
    {% if features.install %}
    - Temporarly install new packages by the user
    {% endif %}
    {% if features.shared_folder %}
    - Shared folder exists
    {% endif %}
    {% if features.persistent_storage %}
    - Persistent storage
    {% endif %}
    {% for feature in features.misc %}
    - {{ feature }}
    {% endfor %}

{% if (features.programming_languages or features.environments) %} 
=== "Kernels :material-information-outline:{ title="Links to Kernels" }" 
    {% if features.programming_languages %}
    Programming Languages:
    {% for kernel in features.programming_languages %}
    {% if Links[kernel | lower] %}
    - [{{ kernel }}]({{ Links[kernel | lower] }})
    {% else %}
    - {{ kernel }}
    {% endif %}
    {% endfor %}
{% endif %}
    {% if features.environments %} 
    Environments:
    {% for kernel in features.environments %}
-   {{ kernel }} {% if Links[kernel] %} [{{ Links[kernel] }}]({{ Links[kernel] }}) 
    {% else %}  
    {% endif %}
    {% endfor %}
    {% endif %}
{% endif %}

{% if features.extensions %}
=== "Extensions"
    {% for extension in features.extensions %}
    - {{ extension }}
    {% endfor %}
{% endif %}

{% if features.proxy_apps %}
=== "Web-proxy Applications"
    {% for app in features.proxy_apps %}
    - {{ app }}
    {% endfor %}
{% endif %}

## Resources
{{ title }} provides Jupyter servers within the following resource limits:

| Resource                           | Default                                 | Maximum                             |
|------------------------------------|-----------------------------------------|-------------------------------------|
| Number of Jupyter servers per user | {{ resources.default_server_user }}     | {{ resources.max_server_user }}     |
| Number of CPUs                     | {{ resources.default_cpu }}             | {{ resources.max_cpu }}             |
| CPU time                           | {{ resources.default_cpu_time }}        | {{ resources.max_cpu_time }}        |
| Amount of memory                   | {{ resources.default_memory }}          | {{ resources.max_memory }}          |
| Number of GPUs                     | {{ resources.default_gpu }}             | {{ resources.max_gpu }}             |
| Disk space                         | {{ resources.default_disk }}            | {{ resources.max_disk }}            |
| Persistent disk space              | {{ resources.default_persistent_disk }} | {{ resources.max_persistent_disk }} |

{% if technicals %}
## Technical
Some technical insights about {{ title }}:
  {% if technicals.platform %}
- Platform: {{ technicals.platform }}
  {% endif %}
  {% if technicals.deployment %}
- Deployment: {{ technicals.deployment }} {% if technicals.deployment_url %} [Further information]({{ technicals.deployment_url }}) {% endif %}
  {% endif %}
  {% if technicals.login_attributes %}
- Required attributes, entitlements or memberships for Login: {{ technicals.login_attributes }}
  {% endif %}
  {% if technicals.hardware_location %}
- Hardware location: {{ technicals.hardware_location }}
  {% endif %}
  {% if technicals.misc %}
  {% for feature in technicals.misc %}
- {{ feature }}
  {% endfor %}
  {% endif %}
{% endif %}
