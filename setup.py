from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/graph'],
    install_requires = ['argparse']
)


#NOTE: Not sure if scripts/graph is correct