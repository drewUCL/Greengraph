from graph import Greengraph
from argparse import ArgumentParser
from matplotlib import pyplot as this_plot

def main():
   ''' 
       Command Line Interface Allowing The User To Specify Arguments 
       This Function Then Plots The Results Where The Package Was Called From
	   For Example, If It Was Called From The Desktop, The Resulting Chart Would Be Saved On The Desktop For The User.
   '''
   
   parser = ArgumentParser(description = "Generate Green Density Chart Based on Two Points")
   
   parser.add_argument('--from', '-f',help='Enter a start location here such as London', dest='startPoint')
   parser.add_argument('--to', '-t',help='Enter an end location here such as Oxford', dest='endPoint') 
   parser.add_argument('--steps', '-s', type=int, help='Enter the number of steps you wish to chart', default=10)
   parser.add_argument('--out', '-o', help='Enter the file name you wish to call the image (Default=PNG)', default='output.png')
   
   arguments= parser.parse_args()
   
   this_chart = Greengraph(arguments.startPoint,arguments.endPoint)
   this_data = this_chart.green_between(arguments.steps)
   this_plot.plot(this_data)
   this_plot.savefig(arguments.out)