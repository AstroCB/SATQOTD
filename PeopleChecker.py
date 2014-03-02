import json
import urllib
import time

people = 0

check_num = 3000 #raw_input("Enter number of people to check for")

while people < check_num:
	results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))

	results = results['results']
	results = results['Question Data']
	time.sleep(1.5)
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

	people = int(temp)
	time.sleep(5)

results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))
print results['lastsuccess']
