# Lastlogcsv

[![Tests result](https://github.com/Dashstrom/lastlogcsv/actions/workflows/tests.yml/badge.svg)](https://github.com/Dashstrom/lastlogcsv/actions/workflows/tests.yml)
[![Build result](https://github.com/Dashstrom/lastlogcsv/actions/workflows/publish.yml/badge.svg)](https://github.com/Dashstrom/lastlogcsv/actions/workflows/publish.yml)

Converter from /var/log/lastlog to csv file.

## Install from PyPI

```sh
pip3 install lastlogcsv
```

## Install from Github

```sh
pip3 install git+https://github.com/Dashstrom/lastlogcsv
```

## Usage

You can run the script with `lastlogcsv` or `python3 -m lastlogcsv`

```txt
usage: lastlogcsv [-h] [-i INPUT] [-o OUTPUT] [-s {L,A}] [-e]

Converter file from /var/log/lastlog to csv file.

The output format is `uid,timestamp,tine,host`.
Exemple : `1000,1582898351,pts/0,192.168.56.1`

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        lastlog file, /var/log/lastlog by default on unix system
  -o OUTPUT, --output OUTPUT
                        destination for CSV file
  -s {L,A}, --struct {L,A}
                        'A' for actual struct, 'L' for legacy
  -e, --error           display complete error
```
