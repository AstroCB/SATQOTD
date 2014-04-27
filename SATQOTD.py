import json
import urllib

q = raw_input("Would you like to answer today's question? Y/N   ")
q = q.upper()

if q == 'Y':
	response = json.load(urllib.urlopen("http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce"))
else:
	q = raw_input("Enter the day of the question you would like to answer\nFormat: mm/dd/yyyy   ")
	month = q[0] + q[1]
	day = q[3] + q[4]
	year = q[6] + q[7] + q[8] + q[9]

	url = "http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce&kimpath2=sat-question-of-the-day?questionId=" + year + month + day + "&oq=1"
	response = json.load(urllib.urlopen(url))
	print url

print "                   ----" + response['name'] + "----"
print "----Last updated: " + response['lastsuccess'] + "----\n"

results = response['results']
qresults = results['Question Data']
first_results = qresults[0]

date = first_results['Date']
directions = first_results['Directions']
stats = first_results['Stats']
typeques = first_results['Type of Question']
question = first_results['Question']
tries = ""
percent = ""

checking = True
i = 0
x = 0

while checking:
	x = stats[i]
	if x != " ":
		tries += x
	else:
		checking = False
	i += 1

checking = True
now_checking = False

i = 0
y = 0

while checking: #This gets a bit complicated; the data I'm parsing reads "xx,xxx responses \nxx% correct"; I'm looking for the 'xx%', so I want to start adding to percent if it's after \n and stop at the space after the '%'; probably a better way to do this
	for x in stats:
		if x == "\n" and y > 0:
			now_checking = True
		elif x == "\n":
			y += 1
		if now_checking:
			if x == " ":
				now_checking = False
				checking = False
			if now_checking:
				percent += x

temp = ""

percent = percent.split()

for i in percent:
	if i != " " and i != "\n":
		temp += i

percent = str(temp)


temp = ""

for x in date:
	if x != "\n":
		temp += x
	else:
		temp += " "

date = temp



print "Hello. Welcome to your daily SAT training. Today is " + date + ". Your mission, should you choose to accept it, will be to answer this question, which is classified as: " + typeques + ".\n"
print "Warning. This mission is dangerous. " + tries + " people have tried and " + percent + " of them have survived (okay, gotten it correct).\n"
print "Here is your briefing: \n" + directions + "\n"

validans = False
resp = True

#while not(validans):
#	start = raw_input("Ready to begin? Type yes or no.")
#	if start.upper() == 'YES':
#		validans = True
#		resp = True
#	elif start.upper() == 'NO':
#		validans = True
#		resp = False
#	else:
#		print "Sorry. Try again:\n"


if resp == True:
	print question

	aresults = results["Answer Data"]

	for i in aresults:
		print i['Answers']
