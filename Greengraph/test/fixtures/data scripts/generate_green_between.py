import geopy
import requests
from StringIO import StringIO # A library to convert between files and strings
import numpy as np # A library to deal with matrices
from matplotlib import image as img # A library to deal with images

geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

def location_sequence(start, end, steps):
  lats = np.linspace(start[0], end[0], steps) # "Linearly spaced" data
  longs = np.linspace(start[1],end[1], steps)
  return np.vstack([lats, longs]).transpose()
  
  
def is_green(pixels):
    threshold=1.1
    greener_than_red = pixels[:,:,1] > threshold* pixels[:,:,0]
    greener_than_blue = pixels[:,:,1] > threshold*pixels[:,:,2]
    green = np.logical_and(greener_than_red, greener_than_blue) 
    return green
	
def request_map_at(lat,long, satellite=True,zoom=10,size=(400,400),sensor=False):
  base="http://maps.googleapis.com/maps/api/staticmap?"
  
  params=dict(
    sensor= str(sensor).lower(),
    zoom= zoom,
    size= "x".join(map(str,size)),
    center= ",".join(map(str,(lat,long))),
    style="feature:all|element:labels|visibility:off"
  )
  if satellite:
    params["maptype"]="satellite"

  return requests.get(base,params=params)

def map_at(*args,**kwargs):
    return request_map_at(*args,**kwargs).content
	
def count_green_in_png(data):
    pixels=img.imread(StringIO(data)) # Get our PNG image as a numpy array
    return np.sum(is_green(pixels))
	
def geolocate(place):
  return geocoder.geocode(place, exactly_one = False)[0][1]

def green_between(start, end,steps):
    return [count_green_in_png(map_at(*location))
            for location in location_sequence(
                            geolocate(start),
                            geolocate(end),
                            steps)]


if __name__ == "__main__":
	myfile = open('green_between_data.txt','w')
	test_locations_from = [ 'London', 'Glasgow', 'Rome' ]
	test_locations_to = [ 'Edinburgh', 'Paris', 'Chicago']
	for i in range(0,len(test_locations_from)):
		tFrom = test_locations_from[i]
		tTo = test_locations_to[i]
		theGreen = green_between(tFrom, tTo, 10)
		myfile.write("From: " + tFrom + "\n")
		myfile.write("To: " + tTo + "\n")
		for j in range(0,len(theGreen)):
			myfile.write(str(theGreen[j]) + "\n")
		myfile.write("\n")
	print "Complete..."
	
	
	
	
	


