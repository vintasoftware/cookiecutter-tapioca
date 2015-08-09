# coding: utf-8

import unittest

from tapioca_{{ cookiecutter.service_name|lower|replace(' ', '_') }} import {{ cookiecutter.service_name|title|replace(' ', '') }}


class TestTapioca{{ cookiecutter.service_name|title|replace(' ', '') }}(unittest.TestCase):

    def setUp(self):
        self.wrapper = {{ cookiecutter.service_name|title|replace(' ', '') }}()


if __name__ == '__main__':
    unittest.main()
