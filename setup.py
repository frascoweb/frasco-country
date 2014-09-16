from setuptools import setup, find_packages


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-assets',
    version='0.1',
    url='http://github.com/frascoweb/frasco-assets',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="pycountry integration for Frasco",
    long_description=desc(),
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'frasco',
        'pycountry==1.8'
    ]
)