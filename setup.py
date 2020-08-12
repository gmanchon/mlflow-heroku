from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'mlflow==1.8.0']

setup(
    name='WagonDataMLFlowTmp',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Wagon Data MLFlow Tmp'
)
