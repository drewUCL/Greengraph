import geopy
import numpy as np

def geolocate(place):
	geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
        return geocoder.geocode(place, exactly_one=False)[0][1]

def location_sequence(start, end, steps):
  	lats = np.linspace(start[0], end[0], steps) # "Linearly spaced" data
  	longs = np.linspace(start[1],end[1], steps)
  	return np.vstack([lats, longs]).transpose()

if __name__ == "__main__":
	myfile = open('sequence_list.txt','w')
	location_matrix = location_sequence(geolocate("London"), geolocate("Edinburgh"), 5)
	myfile.write("Start: London \n")
	for i in range(0,len(location_matrix)):
		for j in range(0,len(location_matrix[i])):
			myfile.write(str(location_matrix[i][j]))
			if j == 0: myfile.write(',')
		myfile.write("\n")
	myfile.write("End: Edinburgh")
	print 'Complete...'