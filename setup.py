from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

# This function reads requirements.txt and returns a clean list
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        requirements = f.readlines()
        
        # Clean lines
        requirements = [req.strip() for req in requirements if req.strip()]
        
        # Remove '-e .'
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Harshavardhan',
    author_email='tharshavardhan613@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)