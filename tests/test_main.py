"""Unit tests for lastlog.__main__."""
import io
import sys
from contextlib import redirect_stdout
from unittest import TestCase, skipIf
from unittest.mock import MagicMock, mock_open, patch

from lastlogcsv.__main__ import main
from tests.utils import LASTLOG_DATA, LASTLOG_OUT, LASTLOG_PATH


class TestMain(TestCase):

    def test_main_input(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            exitcode = main(["-i", LASTLOG_PATH, "-e"])
        self.assertEqual(out.getvalue(), LASTLOG_OUT, "Output mismatch")
        self.assertEqual(0, exitcode, "Command return non-zero exit code")

    @skipIf(sys.version_info < (3, 7), "Can't mock read(n) before python 3.7")
    @patch("builtins.open",
           side_effect=[mock_open(read_data=LASTLOG_DATA).return_value,
                        mock_open().return_value])
    def test_main_output(self, mo: MagicMock) -> None:  # type: ignore
        out = io.StringIO()
        with redirect_stdout(out):
            exitcode = main(["-i", LASTLOG_PATH, "-o", "fakefile", "-e"])
        self.assertEqual(out.getvalue(), "", "No ouput attemp")
        self.assertEqual(0, exitcode, "Command return non-zero exit code")
        mo.assert_called_with("fakefile", "wt", encoding="utf8")
