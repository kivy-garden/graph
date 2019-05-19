kivy-garden demo flower
========================

[![Coverage Status](https://coveralls.io/repos/github/kivy-garden/flower/badge.svg?branch=master)](https://coveralls.io/github/kivy-garden/flower?branch=master)
[![Build Status](https://travis-ci.org/kivy-garden/flower.svg?branch=master)](https://travis-ci.org/kivy-garden/flower)

A kivy garden flower that shows how to add flowers.

Flower information
-------------------

A kivy garden flower demo.

Install
---------

```sh
pip install kivy_garden.flower
```

#### Usage

```py
do_something
```

TODO
-------

* add your code

Contributing
--------------

Check out our [contribution guide](CONTRIBUTING.md) and feel free to improve the flower.

License
---------

This software is released under the terms of the MIT License.
Please see the [LICENSE.txt](LICENSE.txt) file.

How to release
===============

* update `__version__` in `kivy-garden/flower/__init__.py` to the latest version.
* update `CHANGELOG.md` and commit the changes
* call `git tag -a x.y.z -m "Tagging version x.y.z"`
* call `python setup.py bdist_wheel --universal` and `python setup.py sdist`, which generates the wheel and sdist in the dist/* directory
* Make sure the dist directory contains the files to be uploaded to pypi and call `twine check dist/*`
* then call `twine upload dist/*` to upload to pypi.
* call `git push origin master --tags` to push the latest changes and the tags to github.
