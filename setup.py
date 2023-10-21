from setuptools import find_packages,setup

from typing import List

dot ='-e .'

def get_requirements(file_path:str)->List[str]:
    req=[]
    with open(file_path) as f:
        req=f.readlines()
        req=[i.replace('\n','') for i in req]
        if dot in req:
            req.remove(dot)
    return dot

setup(
    name='Summarization',
    version='0.0.1',
    author='Vipin',
    author_email='tanwarvipin1105@gmail.com',
    pack=get_requirements('requirements.txt'),
    packages=find_packages()

)