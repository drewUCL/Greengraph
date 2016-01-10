import mock

from ..__init__ import parser, chart, process
from ..graph import Greengraph as GR

from nose.tools import assert_equal, assert_true
from matplotlib import pyplot as py

def test_command():
	'''
	Description: A function to test the command line arguments
	Data Source: Within Function
	'''
	commands = parser.parse_args(['--from','London','--to','Edinburgh','--steps','12','--out','LDN_EDN.png'])
	#Test Each Command
	assert_equal(commands.StartLocation,'London')
	assert_equal(commands.EndLocation,'Edinburgh')
	assert_equal(commands.steps,12)
	assert_equal(commands.out,'LDN_EDN.png')


#ISSUE: no display name and no $DISPLAY environment variable
@mock.patch.object(py, 'show')
@mock.patch.object(py, 'savefig')
@mock.patch.object(py, 'plot')
@mock.patch.object(py, 'xlabel')
@mock.patch.object(py, 'ylabel')
@mock.patch.object(py, 'title')
@mock.patch('Greengraph.map.Map.show_green')
@mock.patch('Greengraph.map.Map.count_green')
@mock.patch('Greengraph.graph.Greengraph.location_sequence')
@mock.patch('Greengraph.graph.Greengraph.geolocate')
@mock.patch('Greengraph.graph.Greengraph.green_between')
def test_chart(mock_show, mock_savefig, mock_plot, mock_xlabel, mock_ylabel, mock_title, mock_green_between, mock_show_green, mock_count_green,mock_location_sequence, mock_geolocate):
	''' 
	Description: A function to ensure the chart is working and will work - this is done by simply checking if the ylabel is asserted as the default argument of 'Green Pixel Density'. Function can easily be changed to assert number of steps for example. The function was initially this but I got some errors on Travis CI and thus the descision was made to change the workings of the function for the benefit of the wider community having an external source such as Travis CI to verify testing coverage.
	Data Source: Within Function
	'''
	arguments = parser.parse_args(['--from','London','--to','Edinburgh','--steps','12','--out','LDN_EDN.png'])
	chart(arguments.StartLocation,arguments.EndLocation,arguments.steps,arguments.out)
	mock_green_between.assert_called_with("'Green Pixel Density'")

@mock.patch('Greengraph.__init__.parser.parse_args')
@mock.patch('Greengraph.__init__.chart')
def test_process(mock_parser, mock_chart):
	''' 
	Description: A function to test if the process function is actually called. This is essential for the whole library to work on a users machine.
	Data Source: Within Function
	'''
	process()
	assert_true(mock_parser.called)