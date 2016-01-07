from nose.tools import assert_almost_equal, assert_in, assert_equal, assert_false, assert_true
from ..graph import Greengraph

import os
import yaml

#Test the Greengraph class initialisation of start and end point
def test_Greengraph():
	''' 
	Description: A function to test the initialisation of Greengraph 
	Data Structure: Static [ within this function ['London','Glasgow'] ]
	'''
	userInput = Greengraph('London','Glasgow')
	assert_equal(userInput.start, 'London')
	assert_equal(userInput.end, 'Glasgow')
	
def test_geolocate():
	''' 
	Description: A function to test multiple locations and analyse the return of geolocate
	Data Source: YAML
	'''
	tObject =  Greengraph(0.0,0.0) #initiate the Greengraph object to access geolocate
	with open(os.path.join(os.path.dirname(__file__),'fixtures','graph_test_data.yaml')) as data:
		test_data = yaml.load(data)['test_geolocate']
		for point in test_data:
			city = point.pop('city')
			latitude = point.pop('latitude')
			longitude = point.pop('longitude')
			assert_equal(tObject.geolocate(city),(latitude,longitude))
	
def test_location_sequence():
	''' [INSERT COMMENT] '''
	pass
	
def test_green_between():
	''' [INSERT COMMENT] '''
	pass
	