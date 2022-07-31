"""Unit tests for lastlog.__main__."""
import io
from contextlib import redirect_stdout
from unittest import TestCase

from lastlogcsv.__main__ import main
from tests.utils import LASTLOG_OUT, LASTLOG_PATH


class TestMain(TestCase):

    def test_main(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            exitcode = main(["-i", LASTLOG_PATH])
        self.assertEqual(out.getvalue(), LASTLOG_OUT, "Output mismatch")
        self.assertEqual(0, exitcode, "Command return non-zero exit code")
