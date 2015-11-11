from argparse import ArgumentParser
from graph import Greengraph

def process():
   parser = ArgumentParser(description = "Generate Green Density Chart Based on Two Points")
   
   #Unsure if these arguments are correct and linking to the correct place - continuing development and will update comment once known
   
   parser.add_argument('--from', '-f')
   parser.add_argument('--to', '-t') #action="store_true"
   parser.add_argument('--steps', '-s')
   parser.add_argument('--out', '-o')

   arguments= parser.parse_args()

   print Greengraph(arguments.from, arguments.to, arguments.steps, arguments.out) #from is also a python command is this an issue

if __name__ == "__main__":
    process()