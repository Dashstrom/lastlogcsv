import os

LASTLOG_OUT = ("1000,1582898351,pts/0,192.168.56.1\n"
               "1001,1582898530,pts/1,192.168.56.1\n")
LASTLOG_PATH = os.path.join(os.path.dirname(__file__), "resources", "lastlog")
with open(LASTLOG_PATH, "rb") as _lastlog:
    LASTLOG_DATA = _lastlog.read()
