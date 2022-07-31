# Lastlog

![Build result](https://github.com/Dashstrom/lastlogcsv/actions/workflows/build_and_publish.yml/badge.svg)

![Tests result](https://github.com/Dashstrom/lastlogcsv/actions/workflows/tests.yml/badge.svg)

This project aims to transform the lastlog files located in /var/log into a CSV file or print in into stdout.

## Usage

```txt
usage: lastlogcsv [-h] [-i INPUT] [-o OUTPUT] [-s {L,A}] [-e ERROR]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        lastlog file, /var/log/lastlog by default
  -o OUTPUT, --output OUTPUT
                        destination for CSV file
  -s {L,A}, --struct {L,A}
                        'A' for actual struct, 'L' for legacy
  -e ERROR, --error ERROR
                        display complete error
```

## Run test

```sh
tox
```

## Install package

```sh
pip install .
```
