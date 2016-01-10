import mock

from ..__init__ import parser, chart, process
from ..graph import Greengraph as GR

from nose.tools import assert_equal, assert_true
from matplotlib import pyplot as py

def test_command():
	'''
	Description: A function to test the command line arguments
	Data: STATIC
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
@mock.patch.object(GR, 'green_between')
@moch.patch('Greengraph.map.Map.show_green')
@moch.patch('Greengraph.map.Map.count_green')
@moch.patch('Greengraph.graph.Greengraph.location_sequence')
@moch.patch('Greengraph.graph.Greengraph.geolocate')
def test_chart(mock_show, mock_savefig, mock_plot, mock_green_between):
	arguments = parser.parse_args(['--from','London','--to','Edinburgh','--steps','12','--out','LDN_EDN.png'])
	chart(arguments.StartLocation,arguments.EndLocation,arguments.steps,arguments.out)
	mock_green_between.assert_called_with((100.12,100.12),(110.34,110.34),12)

@mock.patch('Greengraph.__init__.parser.parse_args')
@mock.patch('Greengraph.__init__.chart')
def test_process(mock_parser, mock_chart):
	process()
	assert_true(mock_parser.called)