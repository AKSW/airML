from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="airML",
    version="0.0.1-alpha",
    author="Lahiru Oshara Hinguruduwa",
    author_email='oshara.16@cse.mrt.ac.lk',
    url='https://github.com/AKSW/airML',
    description="application will allow users to " +
                "share and dereference ML models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['airML'],
    packages=[""],
    package_dir={'': 'src'},
    include_package_data=True,
    license='Apache',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3',
    ],

)
