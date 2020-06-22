from setuptools import setup, find_packages

setup(
    name='jupyfm',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A patch filemanager for jupyter',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/urihoenig/jupyter-file-manager',
    author='Uri Hoenig',
    author_email='urih@iguazio.com'
)
