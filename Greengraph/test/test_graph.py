from nose.tools import assert_almost_equal, assert_in, assert_equal, assert_false, assert_true
from ..graph import Greengraph
from ..map import Map
from matplotlib import image as img #change

import os
import yaml
import numpy
import geopy
import requests
import mock

@mock.patch.object(geopy.geocoders, 'GoogleV3')
def test_Greengraph(mock_geocoders):
	''' 
	Description: A function to test the initialisation of Greengraph 
	Data Source: Within Function
	'''
	userInput = Greengraph('London','Glasgow')
	mock_geocoders.assert_equal(userInput.start, 'London')
	mock_geocoders.assert_equal(userInput.end, 'Glasgow')

@mock.patch.object(geopy.geocoders.GoogleV3, 'geocode')
def test_geolocate(mock_geocode):
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
			mock_geocode.assert_equal(tObject.geolocate(city),(latitude,longitude))
	
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

@mock.patch.object(img, 'imread')
@mock.patch.object(requests, 'get')
@mock.patch.object(Greengraph, 'geolocate')
@mock.patch.object(Map, 'count_green')
def test_green_between( mock_geolocate, mock_count_green, mock_imread, mock_get ):
	'''
	Description: This function tests and Mocks the behavour 
	Data Source: YAML	
	'''
	with open(os.path.join(os.path.dirname(__file__),'fixtures','graph_test_data.yaml')) as data:
		test_data = yaml.load(data)['test_green_between']
		for point in test_data:
			tFrom = point.pop('from_point')
			tFromCoord = point.pop('from_locations')
			tTo = point.pop('to_point')
			tToCoord = point.pop('to_location')
			tSteps = point.pop('steps')
			tReturnVector = point.pop('green_vector')
			
			#Mock geoloacte and count_green as we only want to test an isolated event of green_between
			mock_count_green.side_effect = [tFromCoord,tToCoord]
			mock_geolocate.side_effect = tReturnVector
			#Get test pixel result
			gPixel = Greengraph(tFrom,tTo).green_between(tSteps)
			assert_equal(tReturnVector,gPixel)
