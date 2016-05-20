import urllib

apiUrl = "https://source.unsplash.com/random/1920x1080"

for x in range(0, 10):
	print "Retrieving image: {0}/10".format(str(x+1))
	urllib.urlretrieve(apiUrl, "C:/Users/Dan/Documents/Projects/new_tab/bck_images/{0}.jpg".format(x))

