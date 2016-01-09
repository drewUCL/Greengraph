from ..map import Map
from ..graph import Greengraph
from nose.tools import assert_equal, assert_raises
from matplotlib import image as im

import unittest 
import yaml
import os
import numpy as np
import mock
import requests
import png #pip install pypng


@mock.patch.object(requests,'get')
@mock.patch.object(im,'imread')
def test_map(mock_imread,mock_get):
	'''
	Description: 
	Data: YAML
	'''
	with open(os.path.join(os.path.dirname(__file__),'fixtures','map_test_data.yaml')) as data:
		test_data = yaml.load(data)['test_map']
		count = 1
		for point in test_data:
			if (count == 2):
				mock_get_map = Map( point.pop('latitude'),point.pop('longitude'),satellite = False)
			elif (count == 3):
				mock_get_map = Map( point.pop('latitude'),point.pop('longitude'),sensor = True)
			elif (count == 4):
				mock_get_map = Map( point.pop('latitude'),point.pop('longitude'),size = (100,200))
			elif (count == 5):
				mock_get_map = Map( point.pop('latitude'),point.pop('longitude'),zoom = 20)
			else:
				mock_get_map = Map( point.pop('latitude'),point.pop('longitude')) #Called for use in mock_get
			mock_get.assert_called_with( point.pop('url'),params=point.pop('params'))
			count += 1

def test_green():
	'''
	Description: This function tests the green() function with blanket colours - solid green, solid red and solid blue
	Data: YAML
	'''
	with open(os.path.join(os.path.dirname(__file__),'fixtures','map_test_data.yaml')) as data:
		test_data = yaml.load(data)['test_green']
		threshold = 0.9 #standardised in this test
		size = (400,400) #standardised in this test
		for point in test_data:
			pixel_matrix = np.zeros((size[0],size[1], 3)) #standardised in this test
			Mapping = Map(point.pop('latitude'),point.pop('longitude'))
			colour = point.pop('pixel_colour')
			if(colour=="red"):
				pixel_matrix[:, :, 0] = 1
				Mapping.__setattr__('pixels',pixel_matrix)
				assert_equal(Mapping.green(threshold).all(),False)
			elif(colour=="green"):
				pixel_matrix[:, :, 1] = 1
				Mapping.__setattr__('pixels',pixel_matrix)
				assert(Mapping.green(threshold).all())
			elif(colour=="blue"):
				pixel_matrix[:, :, 2] = 1
				Mapping.__setattr__('pixels',pixel_matrix)
				assert_equal(Mapping.green(threshold).all(),False)

def process_data(px,option):
	if (option == 0):
		pixels = ([[0.0,1.0,0.0]] * px) + ([[1.0,1.0,1.0]] * (100-px))
	elif (option == 1):
		pixels = ([[0.0,1.0,0.0]] * px) + ([[0.0,0.0,0.0]] * (100-px))
        pixels = np.array(pixels)
        return pixels.reshape(10,10,3)

def test_count_green():
    MockMap = Map(20.123,15.123)
    option = 0
    for px in range(1,100):
        MockMap.pixels = process_data(px,option)
        assert_equal(MockMap.count_green(), px)

@mock.patch.object(requests,'get')
@mock.patch.object(im,'imread')
@mock.patch.object(im,'imsave')
def test_show_green(mock_imsave,mock_imread,mock_get):
    MockMap = Map(20.123,15.123)
    option = 1
    for px in range(1,100): 
        MockMap.pixels = process_data(px,option)
        MockMap.show_green()
        assert np.array_equal(mock_imsave.call_args[0][1],process_data(px,option))
    assert_equal(mock_imsave.call_args[1], {'format':'png'})

	
	
				
			
			
