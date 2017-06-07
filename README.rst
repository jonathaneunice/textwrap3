
| |travisci| |version| |versions| |impls| |wheel| |coverage|

.. |travisci| image:: https://api.travis-ci.org/jonathaneunice/textwrap3.svg
    :target: http://travis-ci.org/jonathaneunice/textwrap3

.. |version| image:: http://img.shields.io/pypi/v/textwrap3.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/textwrap3

.. |versions| image:: https://img.shields.io/pypi/pyversions/textwrap3.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/textwrap3

.. |impls| image:: https://img.shields.io/pypi/implementation/textwrap3.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/textwrap3

.. |wheel| image:: https://img.shields.io/pypi/wheel/textwrap3.svg
    :alt: Wheel packaging support
    :target: https://pypi.python.org/pypi/textwrap3

.. |coverage| image:: https://img.shields.io/badge/test_coverage-99%25-0000FF.svg
    :alt: Test line coverage
    :target: https://pypi.python.org/pypi/textwrap3


``textwrap3`` is a compatibility back-port of Python 3.6's ``textwrap``
module that supports Python 2.6 forward. This makes a few new
APIs such as ``shorten`` and the ``max_lines`` parameter available
in a compatible way to all Python's in notable current use.

Import and use it just as you would textwrap:

    from textwrap3 import wrap

    text = 'long text here...'
    print(wrap(text, 40))

By design, Python 3 sensibilities and expecations rule whenever
feasible. Especially when wrapping text that includes Unicode
characters, ``textwrap3``'s results may differ from those of the
``textwrap`` of the underlying Python version.  In particular,
``textwrap3`` uses the ``re.UNICODE`` flag so that non-ASCII
characters such as accented letters are considered legitimate word
characters.

It also adds one tweak, considering the Unicode em-dash 
(``'\N{EM DASH}'`` or ``u'\u2014'``) identical to the simulated ASCII em-dash
``--``.

Notes
=====

* See ``CHANGES.yml`` for the Change Log.

* This module is almost entirely the work of Gregory P. Ward
  (``textwrap``'s original author) plus enhancements from the Python
  community.  This separate packaging is just a delivery and
  compatibility vehicle. It contributs cross-Python
  version compatibility shims, a few dditional tests, and better
  handling of real em-dashes. The vast majority of functionality
  still comes from the standard ``textwrap`` code base, as of the
  Python 3.6 release.

Installation
============

To install or upgrade to the latest version::

    pip install -U textwrap3 

You may need to prefix these with ``sudo`` to authorize
installation. In environments without super-user privileges, you may want to
use ``pip``'s ``--user`` option, to install only for a single user, rather
than system-wide. Depending on your system configuration, you may also
need to use separate ``pip2`` and ``pip3`` programs to install for Python 
2 and 3 respectively.

