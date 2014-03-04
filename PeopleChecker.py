import json
import urllib
import time

people = 0

check_num = 14700 #or raw_input("Enter number of people to check for:")

while people < check_num:
	results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))

	results = results['results']
	results = results['Question Data']
	time.sleep(2)
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
		time.sleep(3)

	stats = temp
	temp = ""

	for j in stats:
		if j != ",":
			temp += j

	people = int(temp)
	time.sleep(5)

results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))
finished = results['lastsuccess']

temp = ""
checking = True
i = 0
spaces = 0

while checking: #data read in format "day month date year hh:mm:ss GMT+(-)xxxx (timezone)" -> once four spaces have registered, it reads in the time to temp until it hits another space before the GMT offset
	x = finished[i]
	if spaces > 3:
		if x != " ":
			temp += x
		else:
			checking = False
	else:
		if x == " ":
			spaces += 1
	i += 1
	#time.sleep(3)

finished = temp

finished = finished.split(":") #time is in format hh:mm:ss, gives array [hh, mm, ss]

x = ""
formatted = []

for x in finished:
	formatted.append(int(x))

hours = formatted[0]
minutes = formatted[1]
seconds = formatted[2]

if hours < 12:
	half_day = 'AM'
	reg_hours = hours
else:
	half_day = 'PM'
	reg_hours = hours - 12

us_eastern = hours - 5
us_central = hours - 6
us_pacific = hours - 8

tmzn = 'eastern' #or raw_input("Enter timezone (if outside US (and you're checking SAT stats?) enter GMT offset)":) #ask for timezone
tmzn = tmzn.upper()
if tmzn == 'EASTERN':
	usertime = us_eastern
elif tmzn == 'CENTRAL':
	usertime = us_central
elif tmzn == 'PACIFIC' or tmzn == 'WESTERN':
	usertime = us_pacific
elif tmzn == " " or tmzn == "":
	usertime = hours
else:
	tmzn.strip(" ")
	tmzn = int(tmzn)
	usertime = hours + tmzn
if usertime < 12:
	half_day = 'AM'
	reg_hours = usertime
else:
	half_day = 'PM'
	reg_hours = usertime - 12

if reg_hours < 0:
	reg_hours += 12
	half_day = 'PM'
elif reg_hours < 1:
	reg_hours = 12

minutes = 9
seconds = 8
reg_hours = str(reg_hours) #formats time units as strings and checks for 0 errors (so there's no 9:3 instead of 9:03 error, which could be caused by the int conversion done on the array elements to be able to perform calculations with them)
minutes = str(minutes)
seconds = str(seconds)

if int(minutes) < 10:
	minutes = '0' + minutes

if int(seconds) < 10:
	seconds = '0' + seconds

print "Reached " + str(check_num) + " people at " + str(reg_hours) + ":" + str(minutes) + ":" + str(seconds) + " " + half_day + "."
