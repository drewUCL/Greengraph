from graph import Greengraph
from argparse import ArgumentParser
from matplotlib import pyplot as this_plot

def chart(start, end, steps, out):
   this_chart = Greengraph(start,end)
   this_data = this_chart.green_between(steps)
   this_plot.plot(this_data)
   #Add Annotations
   this_plot.xlabel("Steps")
   this_plot.ylabel("'Green Pixel Density'")
   this_plot.title("Green Land Density: " + start + " - " + end)
   #Save result and show user
   this_plot.savefig(out)
   this_plot.show()

def process():
   ''' 
       Command Line Interface Allowing The User To Specify Arguments 
       This Function Then Plots The Results Where The Package Was Called From
	   For Example, If It Was Called From The Desktop, The Resulting Chart Would Be Saved On The Desktop For The User.
   '''
   
   parser = ArgumentParser(description = "Generate Green Density Chart Based on Two Points")
   
   #Positional Arguments
   parser.add_argument('--from', help='Enter a start location here such as London. [STRING]', dest='startPoint')
   parser.add_argument('--to', help='Enter an end location here such as Oxford. [STRING]', dest='endPoint') 
   
   #Optional Arguments
   parser.add_argument('--steps', '-s', type=int, help='Enter the number of steps you wish to chart. [INT]', default=10)
   parser.add_argument('--out', '-o', help='Enter the file name you wish to call the image (Default=PNG)', default='output.png')
   
   arguments= parser.parse_args()
   
   chart(arguments.startPoint,arguments.endPoint,arguments.steps,arguments.out)
   