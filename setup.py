#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    lines = requirements.readlines()
    libraries = [lib for lib in lines if not lib.startswith('-')]
    dependency_links = [link.split()[1] for link in lines if 
            link.startswith('-f')]

setup(
    name='django-trustypie',
    version='1.0',
    author='Arnaud Grausem',
    author_email='arnaud.grausem@gmail.com',
    maintainer='Arnaud Grausem',
    maintainer_email='arnaud.grausem@gmail.com',
    url='https://github.com/agrausem/django-trustypie',
    license='PSF',
    description=u'An RSA authentication plugin for django-tastypie',
    long_description=long_description,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    download_url='http://pypi.python.org/pypi/django-trustypie',
    install_requires=libraries,
    dependency_links=dependency_links,
    keywords=['Rsa', 'authentication', 'tastypie', 'Rest API', 'key'],
    entry_points={},
    classifiers = (
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    )
)
