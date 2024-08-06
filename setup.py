from setuptools import find_packages, setup
from typing import List

HYPHEN_AND_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
    requirements = [req.replace("\n", "") for req in requirements]

    if (HYPHEN_AND_DOT in requirements):
        requirements.remove(HYPHEN_AND_DOT)

    return requirements

setup(
    name="cardio-disease-ml-project",
    version="0.0.1",
    author="Vanderval",
    author_email="vander31bs@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
