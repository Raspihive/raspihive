import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="raspihive",
    version="0.0.1",
    author="RaspiHive Team",
    author_email="",
    description="RaspiHive toolkit for IOTA Network Entry Points",
    long_description=long_description,
    long_description_contenxt_type="text/markdown",
    url="https://github.com/raspihive/raspihive",
    packages=["raspihive"],
    install_requires=["","guizero","tk"], # ToDo: add hornetctl here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',
)
