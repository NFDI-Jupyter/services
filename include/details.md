# {{ title }}
The {{ title }} is provided by {{ provider }} and can be reached [here]({{ service_url }}).

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

: {{ documentation_url }}


## Features
{{ title }} offers:

=== "General"

    - Version: {{ features.version }}
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

{% if features.kernels %}
=== "Kernels"

    {% for kernel in features.kernels %}
    - {{ kernel }}
    {% endfor %}
{% endif %}

{% if features.extensions %}
=== "Extensions"

    {% for extension in features.extensions %}
    - {{ extension }}
    {% endfor %}
{% endif %}

{% if features.proxy_apps %}
=== "Webproxy Applications"

    {% for app in features.proxy_apps %}
    - {{ app }}
    {% endfor %}
{% endif %}

## Resources
{{ title }} provides Jupyter servers within the following resource limits:

| Resource | Default | Maximum |
| -------- | ------- | ------- |
| Number of Jupyter servers per user | {{ resources.default_server_user }} | {{ resources.max_server_user }} |
| Number of CPUs | {{ resources.default_cpu }} | {{ resources.max_cpu }} |
| CPU time | {{ resources.default_cpu_time }} | {{ resources.max_cpu_time }} |
| Amount of memory | {{ resources.default_memory }} | {{ resources.max_memory }} |
| Number of GPUs | {{ resources.default_gpu }} | {{ resources.max_gpu }} |
| Disk space | {{ resources.default_disk }} | {{ resources.max_disk }} |
| Persistent disk space | {{ resources.default_persistent_disk }} | {{ resources.max_persistent_disk }} |
