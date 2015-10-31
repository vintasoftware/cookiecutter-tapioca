# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
{% if cookiecutter.use_oauth_2 == 'y' %}
from requests_oauthlib import OAuth2
{% elif cookiecutter.use_oauth_1 == 'y' %}
from requests_oauthlib import OAuth1
{% elif cookiecutter.use_basic_auth == 'y' %}
from requests.auth import HTTPBasicAuth
{% endif %}

from .resource_mapping import RESOURCE_MAPPING


class {{ cookiecutter.service_name|title|replace(' ', '') }}ClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = '{{cookiecutter.api_root_url}}'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super({{ cookiecutter.service_name|title|replace(' ', '') }}ClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        {% if cookiecutter.use_oauth_2 == 'y' %}
        params['auth'] = OAuth2(
            api_params.get('client_id', ''), token={
                'access_token': api_params.get('access_token'),
                'token_type': 'Bearer'})
        {% elif cookiecutter.use_oauth_1 == 'y' %}
        params['auth'] = OAuth1(
            api_params.get('api_key'),
            client_secret=api_params.get('api_secret'),
            resource_owner_key=api_params.get('access_token', ''),
            resource_owner_secret=api_params.get('access_token_secret', ''))
        {% elif cookiecutter.use_basic_auth == 'y' %}
        params['auth'] = HTTPBasicAuth(
            api_params.get('user'), api_params.get('password'))
        {% endif %}

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


{{ cookiecutter.service_name|title|replace(' ', '') }} = generate_wrapper_from_adapter({{ cookiecutter.service_name|title|replace(' ', '') }}ClientAdapter)
