#!/usr/bin/env python

from setuptools import setup
from codecs import open


def lines(text):
    """
    Returns each non-blank line in text enclosed in a list.
    See http://pypi.python.org/pypi/textdata for more sophisticated version.
    """
    return [l.strip() for l in text.strip().splitlines() if l.strip()]


setup(
    name='textwrap3',
    version='0.9.1',
    author='Jonathan Eunice',
    author_email='jonathan.eunice@gmail.com',
    description="textwrap from Python 3.6 backport (plus a few tweaks)",
    long_description=open('README.rst', encoding='utf-8').read(),
    url='https://github.com/jonathaneunice/textwrap3',
    license='Python Software Foundation License',
    py_modules=['textwrap3'],
    setup_requires=[],
    install_requires=[],
    tests_require=['tox', 'pytest', 'coverage', 'pytest-cov'],
    test_suite="test",
    zip_safe=False,
    keywords='text wrap fill textwrap',
    classifiers=lines("""
        Development Status :: 4 - Beta
        Operating System :: OS Independent
        License :: OSI Approved :: Python Software Foundation License
        Intended Audience :: Developers
        Programming Language :: Python
        Programming Language :: Python :: 2
        Programming Language :: Python :: 2.6
        Programming Language :: Python :: 2.7
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.3
        Programming Language :: Python :: 3.4
        Programming Language :: Python :: 3.5
        Programming Language :: Python :: 3.6
        Programming Language :: Python :: Implementation :: CPython
        Programming Language :: Python :: Implementation :: PyPy
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: Text Processing
        Topic :: Text Processing :: Filters
    """)
)
