from setuptools import setup
setup(
{
    name = "nest",
    author = "not provided",
    author_email = "not provided",
    version = "0.0.0",
    description = "not provided",
    long_description = "".join(open("README.md")),
    url = "not provided",
    license = "MIT",
    packages = [
        "nest"
    ],
    entry_points = {
        "console_scripts": {
            "nest": "nest:main"
        }
    }
}
)
