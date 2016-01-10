from argparse import ArgumentParser
from nose.tools import assert_equal

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