#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'spotipy',
    'jsonschema'
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Will Dinkel",
    author_email='wdinkel@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Python package to help keep your Spotify playlist metadata up-to-date when it is modified without your approval.",
    entry_points={
        'console_scripts': [
            'spotiminder=spotiminder.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='spotiminder',
    name='spotiminder',
    packages=find_packages(include=['spotiminder', 'spotiminder.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/willdinkel/spotiminder',
    version='0.1.9',
    zip_safe=False,
)
