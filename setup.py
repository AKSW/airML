from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="airML", 
    version="0.0.1",
    author="Lahiru Oshara Hinguruduwa",
    description="application will allow users to " +
                "share and dereference ML models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License :: 2.0",
        "Operating System :: OS Independent",
    ],
    py_modules= ['airML'],
    packages = [""],
    package_dir = {'':'src'},
    include_package_data=True,
)