# Lastlogcsv

![Tests result](https://github.com/Dashstrom/lastlogcsv/actions/workflows/tests.yml/badge.svg)
![Build result](https://github.com/Dashstrom/lastlogcsv/actions/workflows/publish.yml/badge.svg)

This project aims to transform the lastlog files located in /var/log into a CSV file or print in into stdout.

## Install from github

```sh
pip install git+https://github.com/Dashstrom/lastlogcsv
```

## Install from PyPI

```sh
pip install lastlogcsv
```

## Usage

You can run the script with `lastlogcsv` or `python3 -m lastlogcsv`

```txt
usage: lastlogcsv [-h] -i INPUT [-o OUTPUT] [-s {L,A}] [-e]

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
