import io
from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

about = {}
with io.open("striprtf/_version.py", "r", encoding="utf-8") as f:
    exec(f.read(), about)

setup(
    name="striprtf",
    packages=["striprtf"],
    version=about["__version__"],
    description="A simple library to convert rtf to text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Joshy Cyriac",
    author_email="joshy@posteo.ch",
    url="https://github.com/joshy/striprtf",
    download_url="https://github.com/joshy/striprtf/archive/v%s.tar.gz"
    % about["__version__"],
    keywords=["rtf"],
    scripts=["striprtf/striprtf"],
    license="BSD-3-Clause",
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
