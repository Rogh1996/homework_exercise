from setuptools import setup

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
    packages= ["homework_exercise"],
    package_data={"homework_exercise": ["requirements.txt", "data_file.json", "data_file_2.toml", "LICENSE.txt", "README.md"]},
    include_package_data=True,
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