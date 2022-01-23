from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = "homework_exercise",
    version = "1.0.0",
    url = "http://github.com/Rogh1996/homework_exercise",
    author='Rafał Odziemski',
    author_email='r.odziemski@student.uw.edu.pl',
    description = "homework NYPD 24.01.2022",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages= find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "numpy",
        "toml"
    ]
)