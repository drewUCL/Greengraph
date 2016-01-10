from argparse import ArgumentParser
from nose.tools import assert_equal

def test_command():
	'''
	Description: A function to test the command line arguments
	Data: STATIC
	'''
	parser = ArgumentParser( prog="Greengraph", description = "Generate Green Density Chart Based on Two Points")
   
    parser.add_argument('--from', '-f', help = 'Enter a start location here such as London. [STRING]',dest='StartLocation', required=True)
    parser.add_argument('--to',  '-t', help = 'Enter an end location here such as Oxford. [STRING]',dest='EndLocation', required=True) 
    parser.add_argument('--steps', '-s', type = int, help = 'Enter the number of steps you wish to chart. [INT]', default = 10)
    parser.add_argument('--out', '-o', help = 'Enter the file name you wish to call the image with extension (Default=.png) [STRING]', default = 'output.png')
   
	commands = parser.parse_args(['--from','London','--to','Edinburgh','--steps',12,'--out','LDN_EDN.png'])
	
	assert_equal(commands.StartLocation,'London')
	assert_equal(commands.EndLocation,'London')
	assert_equal(commands.steps,12)
	assert_equal(commands.out,'LDN_EDN.png')