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


@mock.patch.object(py, 'show')
@mock.patch.object(py, 'savefig')
@mock.patch.object(py, 'plot')
@mock.patch.object(GR, 'green_between')
def test_chart(mock_show, mock_savefig, mock_plot, mock_green_between):
	'''
	Description: A function to test if the charting function is in operation
	'''
	arguments = parser.parse_args(['--from','London','--to','Edinburgh','--steps','12','--out','LDN_EDN.png'])
	chart(arguments.StartLocation,arguments.EndLocation,arguments.steps,arguments.out)
	mock_green_between.assert_called_with(12)

@mock.patch('Greengraph.__init__.parser.parse_args')
@mock.patch('Greengraph.__init__.chart')
def test_process(mock_parser, mock_chart):
	process()
	assert_true(mock_parser.called)