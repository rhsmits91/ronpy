import sys

from setuptools import setup

from ronpy import get_version

# ==== SETUP SYSTEM INFORMATION ====
CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)


if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
    ==== unsupported python version ====
    cboe requires Python {}.{}, but you're trying to
    install it on Python {}.{}.""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

VERSION = get_version()
PACKAGE_NAME = 'ronpy'
INSTALL_REQUIRES = []

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description='miscellaneous helper functions',
    author='Ronald Smits',
    packages=[PACKAGE_NAME],
    install_requires=INSTALL_REQUIRES
)
