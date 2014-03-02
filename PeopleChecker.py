import json
import urllib
import time

stats = 0

while stats < 5000:
	results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))

	results = results['results']
	results = results['Question Data']
	results = results[1]

	stats = results['Stats']

	temp = ""
	checking = True
	i = 0

	while checking:
		x = stats[i]
		if x != " ":
			temp += x
		else:
			checking = False
		i += 1
		time.sleep(2)

	stats = temp
	temp = ""

	for j in stats:
		if j != ",":
			temp += j

	stats = int(temp)
	time.sleep(120)

results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))
print results.lastsuccess