from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read().splitlines()

setup(
   name='epub2wavenet',
   version='0.1',
   description='Convert epubs to audiobooks using wavenet',
   author='Anjum',
   packages=['epub2wavenet'],
   install_requires=install_requires,
   scripts=['scripts/generate.py']
)
