from setuptools import setup,find_packages

HYPHEN_E_DOT = "-e ."

def get_long_decription(filepath= "README.md"):
    with open(filepath,'r') as file:
        content = file.read()
        return content
    
def get_requirements(filepath = "requirements.txt"):
    with open(filepath,'r') as file:
        requirements = file.readlines()
        requirements = [r.replace("\n","") for r in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements
    
project_name = "project_name"
__version__ = "0.0.1"
AUTHOR_NAME = "Linkan Kumar Sahu"
AUTHOR_EMAIL = "sahulinkan7@gmail.com",

setup(
    name=project_name,
    version=__version__,
    author= AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    long_description=get_long_decription(),
    packages=find_packages(),
    install_requires = get_requirements()
)