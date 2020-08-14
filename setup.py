import os

from setuptools import setup, find_packages

NAME = "hass-metlink-api"
AUTHOR = "Shane Bennett"
AUTHOR_EMAIL = "smbkiwi@gmail.com"
DESCRIPTION = "An async data manager for the Metlink Wellington API."
URL = "https://github.com/smbkiwi/hass-metlink-api"

REQUIRES = [
    'homeassistant>=0.97.0',
    'http3>=0.6.7',    
]


with open("README.md", "r") as fh:
    long_description = fh.read()

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = {}
with open(os.path.join(HERE, NAME, "__version__.py")) as f:
    exec(f.read(), VERSION)  # pylint: disable=exec-used

setup(
    name=NAME,
    version=VERSION["__version__"],
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    license='Apache Software License',
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",    
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",  
    ],
    install_requires=REQUIRES
)
