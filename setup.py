import setuptools
import os
import re

__project_name__ = "raspihive"

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setuptools.setup(
    name=__project_name__,
    version=get_version(__project_name__),
    author="RaspiHive Team",
    author_email="contact@raspihive.org",
    description="RaspiHive toolkit for IOTA Network Entry Points",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raspihive/raspihive",
    packages=["raspihive"],
    install_requires=[
        "PyQt5",
        "distro==1.5.0"
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',
)
