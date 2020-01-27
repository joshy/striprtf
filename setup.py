from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="striprtf",
    packages=["striprtf"],
    version="0.0.6",
    description="A simple library to convert rtf to text",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Joshy Cyriac",
    author_email="j.cyriac@gmail.com",
    url="https://github.com/joshy/striprtf",
    download_url="https://github.com/joshy/striprtf/archive/v0.0.6.tar.gz",
    keywords=["rtf"],
    scripts=["striprtf/striprtf"],
    classifiers=[],
)
