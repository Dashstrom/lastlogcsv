"""Unit tests for lastlog.parser."""
import io
from contextlib import redirect_stdout
from unittest import TestCase

from lastlogcsv.__main__ import main
from tests.utils import LASTLOG_OUT, LASTLOG_PATH


class TestMain(TestCase):

    def test_main(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            main(["-i", LASTLOG_PATH])
        self.assertEqual(out.getvalue(), LASTLOG_OUT)