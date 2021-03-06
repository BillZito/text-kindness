from flask import Flask, request, redirect
from flask.ext.script import Manager
from flask.ext.script import Command
from twilio.rest import TwilioRestClient
import twilio.twiml
import random

app = Flask(__name__)

manager = Manager(app)
 
#list of numbers to look up upon receiving message
callers = {
    "+14103532508": "BillZ",
    "+14109910925": "Mellie",
    "+14432547513": "BillC",
    "+15206098877": "Olivia",
    "+13019436377": "Hannah",
    "+14138414718": "Alice",
    "+14103530094": "Jenny",
    "+18147772290": "Matt",
    "+17186126814": "Kimmy",
}

#account sid and token

#send morning message
class Send_morning(Command):
	"send a message in the morning"

	def run(self):
		#identify their number
    		from_number = "+14103532508"
    		
	        #if number in our directory above, pick out their name and add it to message string to be sent below
    		if from_number in callers:
        		name = callers[from_number]
    
	        #otherwise, consider them a monkey and respond accordingly
    		else:
        		name = "Monkey" 


		# everything below here is ugly, redundant code, but it was the most efficient as a quick test and will be cleaned up
	        #open and write text to list--should let it throw exception, should let it be personalized based on user
    		#initalize list
    		still_happybillz = []
		still_happyolivia = []
		still_happyalice = []
		still_happyhannah = []
		still_happymellie = []
		still_happyjenny = []
		still_happymatt = []
                still_happykimmy = []    

                #initalize file and then fill the list with the file contents
    		first_file_name = "BillZ.txt"
    		file = open(first_file_name, 'r')    
    		billnum_lines = 0

		#for each line in the file, write it into the list
    		for line in file:
        		still_happybillz.append(line)
        		billnum_lines += 1

		#do the same for olivia and others
		second_file_name = "Olivia" + ".txt"
		second_file = open(second_file_name, 'r')
		olivianum_lines = 0
		
		for line in second_file:
			still_happyolivia.append(line)
			olivianum_lines += 1
		
		third_file_name = "Alice" + ".txt"
		third_file = open(third_file_name, 'r')
		alicenum_lines = 0

		for line in third_file:
			still_happyalice.append(line)
			alicenum_lines += 1

		fourth_file_name = "Mellie" + ".txt"
		fourth_file = open(fourth_file_name, 'r')
		mellienum_lines = 0

		for line in fourth_file:
			still_happymellie.append(line)
			mellienum_lines += 1

		fifth_file_name = "Jenny" + ".txt"
		fifth_file = open(fifth_file_name, 'r')
		jennynum_lines = 0
	
		for line in fifth_file:
			still_happyjenny.append(line)
			jennynum_lines += 1

		sixth_file_name = "Hannah" + ".txt"
		sixth_file = open(sixth_file_name, 'r')
		hannahnum_lines = 0

		for line in sixth_file:
			still_happyhannah.append(line)
			hannahnum_lines += 1
				
		seventh_file_name = "Matt" + ".txt"
                seventh_file = open(seventh_file_name, 'r')
                mattnum_lines = 0
               
                for line in seventh_file:
                        still_happymatt.append(line)
                        mattnum_lines += 1
                       
                eigth_file_name = "Kimmy" + ".txt"
                eigth_file_name = open(eigth_file_name, 'r')
                kimmynum_lines = 0
               
                for line in eigth_file:
                         still_happykimmy.append(line)
                         kimmynum_lines +=1
                 
		#open client and send message
		client = TwilioRestClient(account_sid, auth_token)
                
		for x in (0, 2):
			message = client.messages.create(to="+14103532508", from_="+14437753700", 
					body=still_happybillz[random.randint(0, billnum_lines-1)])

		"""send to Olivia and others"""
		for x in (0, 2):
                        message = client.messages.create(to="+15206098877", from_="+14437753700",
                                        body=still_happyolivia[random.randint(0, olivianum_lines-1)])
			
		for x in (0, 2):
			message = client.messages.create(to="+14138414718", from_="+14437753700",
					body=still_happyalice[random.randint(0, alicenum_lines-1)])

		for x in (0, 2):
			message = client.messages.create(to="+14109910925", from_="+14437753700",
					body=still_happymellie[random.randint(0, mellienum_lines-1)])

		for x in (0, 1):
			message = client.messages.create(to="+14103530094", from_="+14437753700",
					body=still_happyjenny[random.randint(0, jennynum_lines-1)])

		for x in (0,2):
			message = client.messages.create(to="+13019436377", from_="+14437753700",
					body=still_happyhannah[random.randint(0, hannahnum_lines-1)])

                for x in (0,2):
                        message = client.messages.create(to="+18147772290", from_="+14437753700",
                                        body=still_happymatt[random.randint(0, mattnum_lines-1)])

                for x in (0,2):
                        message = client.messages.create(to="+17186126814", from_="+14437753700",
                                        body=still_happykimmy[random.randint(0, kimmynum_lines-1)])


#test of text capability
class Send(Command):
	"send a message to myself"
	
	def run(self):
		client = TwilioRestClient(account_sid, auth_token)
 		message = client.messages.create(to="+14103532508", from_="+14437753700",
                                     body="Hello there!")

#test of any capability
class Hello(Command):
        "prints hello world"

        def run(self):
                print "bill is a boss"


manager.add_command('hello', Hello())
manager.add_command('send', Send())
manager.add_command('send_morning', Send_morning())

if __name__ == "__main__":
	manager.run()
