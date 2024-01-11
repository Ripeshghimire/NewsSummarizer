from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements  = []
    with open(file_path,'r') as file:
        requirements = file.readlines()
        requirements= [requirement.replace("\n","") for requirement in requirements]
    return requirements
setup(
    name = 'NewsSummarizer',
    version='0.0.1',
    author="Ripesh Ghimire",
    author_email="ripeshghimire@gmail.com",
    package = find_packages(),
    install_requires = get_requirements('requirements.txt')
)