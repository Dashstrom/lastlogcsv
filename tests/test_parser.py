"""Unit tests for lastlog.parser."""
import io
from unittest import TestCase

from lastlogcsv import lastlog_to_csv
from tests.utils import LASTLOG_OUT, LASTLOG_PATH


class TestParser(TestCase):

    def test_lastlog_to_csv(self) -> None:
        out = io.StringIO()
        with open(LASTLOG_PATH, "rb") as lastlog_file:
            lastlog_to_csv(lastlog_file, out)
        self.assertEqual(out.getvalue(), LASTLOG_OUT, "Output mismatch")
