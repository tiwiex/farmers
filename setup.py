# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in farmers/__init__.py
from farmers import __version__ as version

setup(
	name='farmers',
	version=version,
	description='For farmer database',
	author='Tiwiex',
	author_email='tiwiex@yahoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
