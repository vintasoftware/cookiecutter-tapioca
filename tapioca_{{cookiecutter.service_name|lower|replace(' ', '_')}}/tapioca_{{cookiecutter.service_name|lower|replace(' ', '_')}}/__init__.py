# coding: utf-8

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


from tapioca_{{ cookiecutter.service_name|lower|replace(' ', '_') }} import {{ cookiecutter.service_name|title|replace(' ', '') }}
