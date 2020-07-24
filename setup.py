import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name = "bs-realpython-reader",
    version = "1.0.1",
    description = "Read the latest Real Python Tutorials",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/srianbury/bs-realpython-reader",
    author = "srian",
    author_email = "bsunbury29@gmail.com",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages = ["reader"], # find_packages(exclude=("tests",)),
    include_package_data = True,
    install_requires = [
        "feedparser",
        "html2text",
        "importlib-resources"
    ],
    entry_points = {
        "console_scripts": [
            "realpython=reader.__main__:main"
        ]
    }
)
