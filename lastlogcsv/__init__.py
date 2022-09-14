"""Main module of lastlogcsv."""
from .parser import (ACTUAL, DEFAULT_LASTLOG, DEFAULT_STYLE, LEGACY,
                     lastlog_to_csv)

__all__ = [
    "ACTUAL",
    "DEFAULT_LASTLOG",
    "DEFAULT_STYLE",
    "LEGACY",
    "lastlog_to_csv"
]

__version__ = "2.0.0"
__author__ = "Dashstrom"
