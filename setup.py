# Responsible for creating the ML model as a package

from setuptools import find_packages, setup
from typing import List

# the following function will return the list of requirements for our project 
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e ')]
    return requirements
setup (
    name='ML-Project',
    version='0.0.1',
    author='Harshit',
    author_email='harshitagrwl911@gmail.com',
    packages=find_packages(),
    # checks all the folders in the current directory and the folder containing 
    # the file '__init__.py' will be taken as a package by find_packages function
    install_requires = get_requirements('requirements.txt')
)
