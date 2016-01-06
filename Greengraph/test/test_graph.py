from nose.tools import assert_almost_equal, assert_in, assert_equal, assert_false, assert_true
from ..graph import Greengraph

''' 
To run the nose tests navigate into tests, then simply type 'nosetests' 
'''

#Test the Greengraph class initialisation of start and end point
def test_Greengraph():
	''' A function to test the initialisation of Greengraph '''
	userInput = Greengraph('London','Glasgow')
	assert_equal(userInput.start, 'London')
	assert_equal(userInput.end, 'Glasgow')
	
def test_geolocate():
	''' [INSERT COMMENT] '''
	pass
	
def test_location_sequence():
	''' [INSERT COMMENT] '''
	pass
	
def test_green_between():
	''' [INSERT COMMENT] '''
	pass
	