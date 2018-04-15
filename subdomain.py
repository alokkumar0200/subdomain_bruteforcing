import requests
from requests.exceptions import ConnectionError

def getUrl(url):
	try:
		r=requests.get(new)
		new1=r.status_code
		if (new1==200 or new1==301):
			return 1
	except ConnectionError:
		return 2


print " ____  _   _ ____  ____   ___  __  __    _    ___ _   _ "
print "/ ___|| | | | __ )|  _ \ / _ \|  \/  |  / \  |_ _| \ | |"
print "\___ \| | | |  _ \| | | | | | | |\/| | / _ \  | ||  \| |"
print " ___) | |_| | |_) | |_| | |_| | |  | |/ ___ \ | || |\  |"
print "|____/ \___/|____/|____/ \___/|_|  |_/_/   \_\___|_| \_|"

	
print " ____  ____  _   _ _____ _____ _____ ___  ____   ____ ___ _   _  ____ "
print "| __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___|_ _| \ | |/ ___|"
print "|  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |    | ||  \| | |  _ "
print "| |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___ | || |\  | |_| |"
print "|____/|_| \_\\\\___/  |_| |_____|_|   \___/|_| \_\\\\____|___|_| \_|\____|"
print""
print""
print""
f = open("subdomain.txt", "r")
name=raw_input("Enter domain Name : \n")
print "\n"

lines = f.readline()
lines=lines.strip()

try:
		
	while lines:
#	lines = f.readline()
#	lines=lines.strip()
	#new="http://"+lines +"."+ name
		new="http://"+lines +"."+ name

		i=getUrl(new)
		new2=lines+"."+name
		
#		new2=lines+"."+name
#		r=requests.get(new)
#		new1=r.status_code
#		if (new1==200):
#			print new

		if(i==1):
			print new2

		lines=f.readline()
		lines=lines.strip()
except ConnectionError:
	pass
