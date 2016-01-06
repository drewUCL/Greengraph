from nose.tools import assert_almost_equal, assert_in, assert_equal, assert_false, assert_true
from ..greengraph import geolocate, maps_url_for, get_map_at
from ..greengraph import count_green, is_green, location_sequence
from ..greengraph import greengraph
from ..graph import Greengraph
from ..map import Map
import png
import os
import yaml

#Test the Greengraph class initialisation of start and end point
def t_Greengraph():
	''' A function to test the initialisation of Greengraph '''
	userInput = Greengraph('London','Glasgow')
	assert_equal(userInput.start, 'London')
	assert_equal(userInput.end, 'Glasgow')
	
def t_geolocate():
	''' [INSERT COMMENT] '''
	pass
	
def t_location_sequence():
	''' [INSERT COMMENT] '''
	pass
	
def t_green_between():
	''' [INSERT COMMENT] '''
	pass
	