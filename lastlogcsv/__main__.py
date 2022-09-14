"""Entry point when the module is launched with `-m lastlogcsv`."""
import argparse
import os
import sys
from traceback import print_exc
from typing import Any, Dict, List, Optional

from .parser import (DEFAULT_LASTLOG, DEFAULT_STYLE, STYLES, StyleKeyType,
                     lastlog_to_csv)


def main(argv: List[str]) -> int:
    """Main method called with by module"""
    parser = argparse.ArgumentParser(
        description=(
            "Converter file from /var/log/lastlog to csv file.\n\n"
            "The output format is `uid,timestamp,line,host`.\n"
            "Exemple : `1000,1582898351,pts/0,192.168.56.1`"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    if os.name == 'nt':
        input_opts: Dict[str, Any] = dict(required=True)
    else:
        input_opts = dict(default=DEFAULT_LASTLOG)
    parser.add_argument(
        "-i", "--input", type=str,
        help="lastlog file, /var/log/lastlog by default on unix system",
        **input_opts
    )
    parser.add_argument("-o", "--output", type=str,
                        help="destination for CSV file")
    parser.add_argument("-s", "--struct", default=DEFAULT_STYLE,
                        choices=STYLES.keys(),
                        help="'A' for actual struct, 'L' for legacy")
    parser.add_argument("-e", "--error", action="store_true",
                        help="display complete error")
    args = parser.parse_args(argv)
    lastlog_path: str = args.input
    csv_path: Optional[str] = args.output
    struct: StyleKeyType = args.struct
    complete_error: bool = args.error
    try:
        with open(lastlog_path, "rb") as lastlog_in:
            if csv_path:
                with open(csv_path, "wt", encoding="utf8") as out:
                    lastlog_to_csv(lastlog_in, out, struct)
            else:
                lastlog_to_csv(lastlog_in, sys.stdout, struct)
    except Exception as err:  # pylint: disable=broad-except
        if complete_error:
            print_exc()
        else:
            print(err, file=sys.stderr)
        return 1
    return 0


def entrypoint() -> None:
    """Entrypoint in script mode."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    entrypoint()
