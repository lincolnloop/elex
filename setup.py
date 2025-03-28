import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="elex",
    version="2.5.0",
    author="Jeremy Bowers, David Eads",
    author_email="jeremy.bowers@nytimes.com, davideads@gmail.com",
    url="https://github.com/newsdev/elex",
    description="Client for parsing the Associated Press's elections API",
    long_description=read("README.rst"),
    packages=["elex", "elex.cli", "elex.api", "tests"],
    entry_points={"console_scripts": ("elex = elex.cli:main",)},
    license="Apache License 2.0",
    keywords="election race candidate democracy news associated press",
    install_requires=[
        "CacheControl",
        "cement<3.0",
        "lockfile",
        "pymongo",
        "python-dateutil",
        "requests",
        "ujson",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
