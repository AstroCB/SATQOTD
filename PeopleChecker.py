import json
import urllib
import time

people = 0

check_num = 3000 #raw_input("Enter number of people to check for")
check_num = 4000 #or raw_input("Enter number of people to check for")

while people < check_num:
	results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))

	results = results['results']
	results = results['Question Data']
	time.sleep(1.5)
	results = results[1]

	stats = results['Stats']
results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))
finished = results['lastsuccess']

	temp = ""
	checking = True
	i = 0
temp = ""
checking = True
i = 0
spaces = 0

	while checking:
		x = stats[i]
while checking: #data read in format "day month date year hh:mm:ss GMT+(-)xxxx (timezone)" -> once four spaces have registered, it reads in the time to temp until it hits another space before the GMT offset
	x = finished[i]
	if spaces > 3:
		if x != " ":
			temp += x
		else:
			checking = False
		i += 1
		time.sleep(2)
	else:
		if x == " ":
			spaces += 1
	i += 1
	#time.sleep(3)

	stats = temp
	temp = ""
finished = temp

	for j in stats:
		if j != ",":
			temp += j
finished = finished.split(":") #time is in format hh:mm:ss, gives array [hh, mm, ss]

	people = int(temp)
	time.sleep(5)
x = ""
time_ready = []

results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))
print results['lastsuccess']
for x in finished:
	time_ready.append(int(x))

hours = time_ready[0]
minutes = time_ready[1]
seconds = time_ready[2]

#us_eastern = hours - 5
#us_central = hours - 6
#us_pacific = hours - 8

#tmzn = 'eastern' #raw_input("Enter timezone (if outside US (and you're checking SAT stats?) enter GMT offset)") #ask for timezone
#tmzn = tmzn.upper()
#if tmzn == 'EASTERN':
#	usertime = us_eastern
#elif tmzn == 'CENTRAL':
#	usertime = us_central
#elif tmzn == 'PACIFIC' or tmzn == 'WESTERN':
#	usertime = us_pacific
#elif tmzn == " " or tmzn == "":
#	usertime = hours
#else:
#	tmzn.strip(" ")
#	tmzn = int(tmzn)
#	usertime = hours - tmzn

print str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"