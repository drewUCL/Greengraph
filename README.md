Greengraph
=============================================

###Introduction
This project radiates around the idea of measuring green pixal density in an attempt to graph how green an area is between two points. The library utilises Google Maps at defined intervals and analyses the green pixel thresholds. These are consequently plotted to visualise the amount of green landmass between two points. 

###Install Instructions
The Greengraph library can be installed using the standard pip command: pip <library>. The installation process is as follows:
- Download Greengraph to your machine
- If the download has been compressed into a zip file, extract
- Go to Greengraph folder root
- Now on your command line:
- **Windows**    : *python Greengraph/setup.py install*
- **Other/Mac**  : *sudo python Greengraph/setup.py install*

The Greengraph library is now ready to use on your machine.

###Example
To use this programme, please follow the steps:

1. Install
2. Enter the two points you wish to analyse (--From ; --To)
3. Select optional arguments (--Steps ; --Out)
4. Your command line should look something like: 

**Greengraph --From 'London' --To 'Edinburgh' --Steps 50 --Out LDN_EDN.png**

The resulting plot will be saved in the root from where the command is called.