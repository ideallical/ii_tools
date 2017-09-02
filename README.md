# ideallical tools

[![build-status-image]][travis]
[![coverage-status-image]][codecov]
[![readthedocs-image]][readthedocs]
[![pypi-version]][pypi]

## Yet another remove capitals except the letters D, S & Q function
Because the world needs less capitals, except D, S & Q.

## Requirements

* Python (2.7, 3.4, 3.5)

## Installation

Install using `pip`...

    pip install ii_tools


## Example

Let's take a look at a quick example of using ii_tools.

    from ii_tools import remove_all_capitals_except_dsq

    remove_all_capitals_except_dsq('Lorem ipsum DunsimQ')

    >>> 'orem ipsum DunsimQ'


# Documentation

Full documentation for the project is available at [ii-tools.readthedocs.io][readthedocs]

# Security

If you believe you've found something in ii_tools which has security
implications, please **do not raise the issue in a public forum**.

Send a description of the issue via email to [ii_tools-security@ideallical.com][security-mail]. The project maintainers will then work with you to resolve any issues where required, prior to any public disclosure.

[travis]: http://travis-ci.org/ideallical/ii_tools?branch=master

[build-status-image]: https://secure.travis-ci.org/ideallical/ii_tools.svg?branch=master
[travis]: http://travis-ci.org/ideallical/ii_tools?branch=master
[security-mail]: mailto:ii_tools-security@ideallical.com
[pypi-version]: https://img.shields.io/pypi/v/ii_tools.svg
[pypi]: https://pypi.python.org/pypi/ii_tools
[coverage-status-image]: https://img.shields.io/codecov/c/github/ideallical/ii_tools/master.svg
[codecov]: http://codecov.io/github/ideallical/ii_tools?branch=master
[readthedocs-image]: https://readthedocs.org/projects/ii-tools/badge/?version=latest
[readthedocs]:https://ii-tools.readthedocs.io/en/latest/
