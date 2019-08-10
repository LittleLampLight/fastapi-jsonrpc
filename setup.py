
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='fastapi-jsonrpc',
    version='0.1.11',
    description='JSON-RPC server based on fastapi',
    python_requires='==3.*,>=3.6.0',
    project_urls={'homepage': 'https://github.com/smagafurov/fastapi-jsonrpc', 'repository': 'https://github.com/smagafurov/fastapi-jsonrpc'},
    author='Sergey Magafurov',
    author_email='magafurov@tochka.com',
    license='MIT',
    keywords='json-rpc asgi swagger openapi fastapi pydantic starlette',
    packages=['fastapi_jsonrpc'],
    package_data={},
    install_requires=['aiojobs==0.*,>=0.2.2', 'fastapi==0.*,>=0.35.0', 'pydantic==0.*,>=0.30.0', 'starlette==0.*,>=0.12.7'],
    extras_require={'dev': ['pygments==2.*,>=2.4.0', 'uvicorn==0.*,>=0.8.6']},
)