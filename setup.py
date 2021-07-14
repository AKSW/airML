from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="airML",
    version="0.0.3",
    author="Lahiru Oshara Hinguruduwa",
    author_email='oshara.16@cse.mrt.ac.lk',
    url='https://github.com/AKSW/airML',
    description="application will allow users to " +
                "share and dereference ML models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['airML'],
    packages=["airML"],
    # package_dir={'': 'airML'},
    package_data={'': ['*.jar']},
    include_package_data=True,
    install_requires=['click>=7.1.2'],
    entry_points={
        'console_scripts': [
            'airML=airML.airML:execute_kbox_command',
        ],
    },
    license='Apache',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3',
    ],

)
