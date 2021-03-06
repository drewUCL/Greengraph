Greengraph <br>
=============================================

<a href="https://travis-ci.org/drewUCL/Greengraph"><img src="https://travis-ci.org/drewUCL/Greengraph.svg?branch=master"></a>
###Introduction
This project radiates around the idea of measuring green pixal density in an attempt to graph how green an area is between two points. The library utilises Google Maps at defined intervals and analyses the green pixel thresholds. These are consequently plotted to visualise the amount of green landmass between two points. 

###Install Instructions
The Greengraph library can be installed using the standard pip command. The installation process is as follows if one simply downloads the zip as supposed to using pip:
- Download Greengraph to your machine from GitHub
- If the download has been compressed into a zip file, extract
- Go to Greengraph folder root
- Now on your command line type:
- **Windows**    : `python Greengraph/setup.py install`
- **Other/Mac**  : `sudo python Greengraph/setup.py install`

**pip install**
- Assuming you have git shell, type: 
`pip install git+https://github.com/drewUCL/Greengraph.git`

The Greengraph library is now ready to use on your machine.

###Example Usage
To use this programme, please follow the steps:

1. Install (*see: Install Instructions*)
2. Enter the two points you wish to analyse (--from ; --to)
3. Select optional arguments (--steps ; --out)
4. Your command line should look something like: 

`Greengraph --from 'London' --to 'Edinburgh' --steps 50 --out LDN_EDN_RESULTS.jpg`

**Output**
<br>
<img src="https://raw.githubusercontent.com/drewUCL/Greengraph/master/Greengraph/Example%20Chart/LDN_EDN_RESULTS.jpg" alt="Result Output">

The resulting plot will be saved where the command is called. <br>
*e.g if you call the package from the desktop, the results file will be output there for the user to view. Additionally the chart will show automatically on the users screen when executed allowing quick and easy analysis.*