from setuptools import setup, find_packages
from typing import List

h='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if h in requirements:
            requirements.remove(h)
    
    return requirements

setup(
    name='ashuML',
    version='0.0.1',
    description='Ashutosh Machine Learning Library',
    author='Ashu Gupta',
    author_email='email.ashu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    )