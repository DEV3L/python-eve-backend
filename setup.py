from setuptools import setup, find_packages

requirements = []

with open('requirements.txt') as file:
    for line in file:
        if line:
            requirements.append(line)

setup(
    name='python-eve-backend',
    packages=find_packages(),
    version='0.1',
    description='Python Eve REST API for managing the data engine for Brain Bit',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    install_requires=[
        requirements
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
