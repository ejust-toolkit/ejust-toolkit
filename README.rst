========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/ejust-toolkit/badge/?style=flat
    :target: https://ejust-toolkit.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/ejust-toolkit/ejust-toolkit/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ejust-toolkit/ejust-toolkit/actions

.. |requires| image:: https://requires.io/github/ejust-toolkit/ejust-toolkit/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/ejust-toolkit/ejust-toolkit/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/ejust-toolkit/ejust-toolkit/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/ejust-toolkit/ejust-toolkit

.. |version| image:: https://img.shields.io/pypi/v/ejust-toolkit.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/ejust-toolkit

.. |wheel| image:: https://img.shields.io/pypi/wheel/ejust-toolkit.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/ejust-toolkit

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ejust-toolkit.svg
    :alt: Supported versions
    :target: https://pypi.org/project/ejust-toolkit

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ejust-toolkit.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/ejust-toolkit

.. |commits-since| image:: https://img.shields.io/github/commits-since/ejust-toolkit/ejust-toolkit/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ejust-toolkit/ejust-toolkit/compare/v0.1.0...main



.. end-badges

eJUST Toolkit for Environmental Justice

* Free software: BSD 3-Clause License

Installation
============

::

    pip install ejust-toolkit

You can also install the in-development version with::

    pip install https://github.com/ejust-toolkit/ejust-toolkit/archive/main.zip


Documentation
=============


https://ejust-toolkit.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
