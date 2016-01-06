from graph import Greengraph
from argparse import ArgumentParser
from matplotlib import pyplot as this_plot
import os

def main():
   parser = ArgumentParser(description = "Generate Green Density Chart Based on Two Points")
   parser.add_argument('--From', '-f',help='Enter a start location here such as London', dest='startPoint')
   parser.add_argument('--To', '-t',help='Enter an end location here such as Oxford', dest='endPoint') 
   parser.add_argument('--Steps', '-s', type=int, help='Enter the number of steps you wish to chart', default=10)
   parser.add_argument('--Out', '-o', help='Enter the file name you wish to call the image (Default=PNG)', default='Images/output.png')
   arguments= parser.parse_args()
   
   this_chart = Greengraph(arguments.startPoint,arguments.endPoint)
   this_data = this_chart.green_between(arguments.Steps)
   this_plot.plot(this_data)
   
   script_location = os.path.dirname(__file__)
   print "SCRIPT LOCATION: %s" % script_location
   results_location = os.path.join(script_location, 'Images/')
   print "RESULTS LOCATION: %s" % results_location
   this_plot.savefig(results_location + arguments.Out)