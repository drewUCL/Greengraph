from nose.tools import assert_almost_equal, assert_in, assert_equal, assert_false, assert_true
from ..graph import Greengraph
from mock import patch

import os
import yaml
import numpy
import geopy


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
	''' 
	Description: A function to test the order of co-ordinates used to generate a path that will allow the image to be generated and then decomposed to analyse the green pixel density.
	Data Source: YAML	
	'''
	tObject =  Greengraph(0.0,0.0) #initiate the Greengraph object to access geolocate
	with open(os.path.join(os.path.dirname(__file__),'fixtures','graph_test_data.yaml')) as data:
		test_data = yaml.load(data)['test_location_sequence']
		for point in test_data:
			tFrom = point.pop('from_point')
			tTo = point.pop('to_point')
			tSteps = point.pop('steps')
			tLocationMatrix = point.pop('location_matrix')
			tResult = tObject.location_sequence(tObject.geolocate(tFrom),tObject.geolocate(tTo),tSteps)
			for row in range(0,len(tResult)):
				for element in range(0,len(tResult[row])):
					assert_almost_equal(tResult[row][element],tLocationMatrix[row][element])

#Patching in .imread and .get 			
@patch('matplotlib.image.imread')
@patch('requests.get')
#Patching created objects: Map && Greengraph
@patch('Map.count_green')
@patch('Greengraph.geolocate')
def test_green_between( mock_geolocate, mock_count_green, mock_imread, mock_get ):
	'''
	Description: This function tests and Mocks the behavour 
	Data Source: YAML	
	'''
	with open(os.path.join(os.path.dirname(__file__),'fixtures','graph_test_data.yaml')) as data:
		test_data = yaml.load(data)['test_green_between']
		for point in test_data:
			tFrom = point.pop('from_point')
			tFromCoord = point.pop('from_location')
			tTo = point.pop('to_point')
			tToCoord = point.pop('to_location')
			tSteps = point.pop('steps')
			tReturnVector = point.pop('green_vector')
			''' 
			Mock the geoloacte and count_green as we only want to test an isolated event of green_between
			'''
			mock_count_green.side_effect = [tFromCoord,tToCoord]
			mock_geolocate.side_effect = tReturnVector
			#get test pixel result
			gPixel = Greengraph(tFrom,tTo).green_between(tSteps)
			assert_equal(tReturnVector,gPixel)
			
			
			
			