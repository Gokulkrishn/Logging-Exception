from setuptools import setup, find_packages

def get_requirements_list():
    '''
    This function returns a list of requirements 
    mentioned in requirements.txt file
    '''
    with open('requirements.txt') as f:
        requirements_list = f.readlines()
        requirements_list = [requirement_name.replace('\n','') for requirement_name in requirements_list]
    return requirements_list

setup(
    name='example',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements_list()
)