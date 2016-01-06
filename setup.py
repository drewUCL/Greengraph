from setuptools import setup, find_packages

setup(
    name = "Greengraph",
	author = "Andrew D. Mann",
	author_email = "Andrew.Mann.15@ucl.ac.uk",
    version = "0.1",
	description = "This package will graph the quantity of green pixles relating to green land from one location to another",
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse','numpy','requests','geopy','matplotlib'],
	entry_points = {
		'console_scripts': [ 
			'greengraph = greengraph:main',
		],
	},
	license = 'MIT',
)