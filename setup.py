#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import sys
sys.path.append('./tests')


setup(
	name= 'shabinary', # Application name:
	version= '0.1.4', # Version number

	author= 'Masayuki Tanaka', # Author name
	author_email= 'm@like.silk.to', # Author mail	

	url='https://github.com/likesilkto/shabinary', # Details
	description='Secure Hash Algorithm library for binary data.', # short description
	long_description='Secure Hash Algorithm library for binary data.', # long description
	install_requires=[ # Dependent packages (distributions)
		'numpy',
	],
	
	include_package_data=False, # Include additional files into the package
	
	#packages=find_packages(exclude=('tests', 'docs')),
	packages = ['shabinary'],
	package_dir={'shabinary':''},
    
    
	test_suite = 'tests',

	classifiers=[
		'Programming Language :: Python :: 3.6',
		'License :: OSI Approved :: MIT',
    ]
)

# uninstall
# % python setup.py install --record installed_files
# % cat installed_files | xargs rm -rf
# % rm installed_files

