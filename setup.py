
from setuptools import setup

setup(
    name = "nest",
    author = "Ramon Moraes",
    author_email = "vyscond@gmail.com",
    version = "0.2.0",
    description = "minimalistic setup manager for python package projects",
    long_description = "".join(open("README.md")),
    keywords = "scaffolding setup package library module",
    url = "vyscond.com/nest",
    license = "MIT",
    packages = [
        "nest"
    ],
    entry_points = {
        "console_scripts": [
            "nest=nest:main"
        ]
    },
    extras_require = {
        "dev": [
            "flake8"
        ]
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ]
)
