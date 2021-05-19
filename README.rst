===========
spotiminder
===========


.. image:: https://img.shields.io/pypi/v/spotiminder.svg
        :target: https://pypi.python.org/pypi/spotiminder

.. image:: https://img.shields.io/travis/willdinkel/spotiminder.svg
        :target: https://travis-ci.com/willdinkel/spotiminder

.. image:: https://readthedocs.org/projects/spotiminder/badge/?version=latest
        :target: https://spotiminder.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A Python package to help keep your Spotify playlist metadata up-to-date when it is modified without your approval.


* Free software: MIT license
* Documentation: https://spotiminder.readthedocs.io.


Features
--------

* Store your playlist ids, names and descriptions in a JSON file. See *playlistMetadataExample.json* for an example.
* The program will run continuously, checking your playlist names and descriptions against the metadata. If any discrepancies are found, both the name and description will be updated.
* If an image folder is specified and contains a JPEG cover image for a playlist, it will get uploaded too (max 256KB size). Image files must be named *<playlistId>.jpg*, replacing *<playlistId>* with your playlist's 22-character id.
* Checks are performed every 60 seconds by default. This is configurable, but don't set it too low or you'll run into API rate limits.

Prerequisites
-------------

* You'll need to `create your own app`_ on the 'Spotify for Developers' portal. Once created, you'll need your app's 'Client ID' and 'Client Secret' in order to run the program. You will also need to set your app's 'Redirect URI' to 'http://localhost:8080'. This is the default used by *spotiminder*. If you would like to set this to something else, feel free to do so. You'll just need to specify the new URI at the command-line when you run the program.
* Python 3. You can `get it here`_. On a Mac it's highly recommended to `follow these instructions`_.

.. _`create your own app`: https://developer.spotify.com/dashboard/applications
.. _`get it here`: https://www.python.org/downloads/
.. _`follow these instructions`: https://opensource.com/article/19/5/python-3-default-mac

Installation
------------

#. Clone or download the repo.
#. Change directory into the root of the repo.
#. Recommended but not required: use *virtualenv* to create a virtual Python environment:

   .. code-block::

      pip install virtualenv
      virtualenv venv
      source venv/bin/activate

#. Install *spotiminder*:

   .. code-block::

      python setup.py install

Usage
-----

``spotiminder -h`` is your friend. The simplest usage is:

.. code-block::

  spotiminder <client id> <client secret> <path to json metadata>

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
