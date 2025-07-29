"""Tracking mechanical properties over time."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("mechanotrack")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Kevin Yamauchi"
__email__ = "kevin.yamauchi@gmail.com"
