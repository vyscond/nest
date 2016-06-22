from setuptools import setup


cfg = {

    name: "nest",
    author: "Ramon Moraes",
    author_email: "vyscond@gmail.com",
    version: "0.0.0",
    description: "not provided",
    long_description: "".join(open("README.md")),
    url: "not provided",
    license: "MIT",
    packages: [
        "nest"
    ],
    entry_points: {
        "console_scripts": [
            "nest=nest:main"
        ]
    }

}

setup(**cfg)
