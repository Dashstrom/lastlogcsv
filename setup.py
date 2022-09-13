import re

from setuptools import find_packages, setup


def read(path):
    # type: (str) -> str
    with open(path, "rt", encoding="utf8") as f:
        return f.read().strip()


def version():
    # type: () -> str
    match = re.search(r"__version__\s+=\s+[\"'](.+)[\"']",
                      read("lastlogcsv/__init__.py"))
    if match is not None:
        return match.group(1)
    return "0.0.1"


setup(
    name="lastlogcsv",
    version=version(),
    author="Dashstrom",
    author_email="dashstrom.pro@gmail.com",
    url="https://github.com/Dashstrom/lastlogcsv",
    license="GPL-3.0 License",
    packages=find_packages(exclude=("tests",)),
    description="Converter from /var/log/lastlog to csv file.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    python_requires=">=3.6.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux"
    ],
    test_suite="tests",
    keywords=["lastlog", "parser", "script", "forensics", "csv"],
    install_requires=read("requirements.txt").split("\n"),
    platforms="any",
    include_package_data=True,
    package_data={
        "lastlogcsv": ["py.typed"],
    },
    entry_points={
        "console_scripts": [
            "lastlogcsv=lastlogcsv.__main__:entrypoint",
        ]
    },
    zip_safe=True
)
