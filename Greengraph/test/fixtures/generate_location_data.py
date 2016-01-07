import geopy

def geolocate(place):
	geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
        return geocoder.geocode(place, exactly_one=False)[0][1]

if __name__ == "__main__":
	locations = ['Glasgow','Edinburgh','Manchester','London','Paris','Naples','Istanbul','Kuching','San Francisco']
	myfile = open('location_list.txt','w')
	for i in range(0,len(locations)):
		myfile.write(locations[i] + ":")
		lat_long = geolocate(locations[i])
		for j in range(0,len(lat_long)):
			myfile.write("\n")
			myfile.write(str(lat_long[j]))
		myfile.write("\n")
	myfile.close()
	print "Complete..."