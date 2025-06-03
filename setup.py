from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
  try:
    with open('requirements.txt','r') as file:
      requirments_list = [
        line.strip() for line in file.readlines()
        if line.strip() and line.strip() != '-e .'
      ]
    return requirments_list
  except FileNotFoundError:
    print('requirements.txt file not found')
    return []


setup (
  name= "langgraph-multiagent-system",
  version = '0.0.1',
  author = 'Vishnuprasad',
  author_mail = 'vishnuprasadvbhat@gmail.com',
  packages = find_packages(),
  install_requires = get_requirements(),
  python_requires = ">=3.10"
)