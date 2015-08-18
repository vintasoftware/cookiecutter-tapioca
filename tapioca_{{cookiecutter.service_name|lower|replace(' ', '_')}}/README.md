# Tapioca {{ cookiecutter.service_name }}

## Installation
```
pip install tapioca-{{ cookiecutter.service_name|lower|replace(' ', '-') }}
```

## Documentation
``` python
from tapioca_{{ cookiecutter.service_name|lower|replace(' ', '_') }} import {{ cookiecutter.service_name|title|replace(' ', '') }}

{% if cookiecutter.use_oauth_2 == 'y' %}
api = {{ cookiecutter.service_name|title|replace(' ', '') }}(
	client_id='{your-client-id}', access_token='{any-valid-access-token}')
{% elif cookiecutter.use_oauth_1 == 'y' %}
api = {{ cookiecutter.service_name|title|replace(' ', '') }}(
	api_key='{your-api-id}',
    api_secret='{your-api-secret}',
    access_token='{your-access-token}',
    access_token_secret='{your-access-token-secret}')
{% elif cookiecutter.use_basic_auth == 'y' %}
api = {{ cookiecutter.service_name|title|replace(' ', '') }}(
	user='{your-user}', password='{your-password}')
{% else %}
api = {{ cookiecutter.service_name|title|replace(' ', '') }}()
{% endif %}
```

No more documentation needed.

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/latest/quickstart/)
- Explore this package using iPython
- Have fun!
