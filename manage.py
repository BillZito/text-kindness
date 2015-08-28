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
}

#account sid and token
account_sid = "AC391d717b317d85ec6bc4278575769ab2"
auth_token = "e306bcddeef2de9a43a7fac69c835eec"

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


	        #open and write text to list--should let it throw exception, should let it be personalized based on user
    		#initalize list
    		still_happybill = []
		still_happyolivia = []
		still_happy2 = []
		still_happy3 = []
		still_happy4 = []
		still_happy5 = []
		still_happy6 = []
    
                #initalize file and then fill the list with the file contents
    		new_file_name = name + "friend.txt"
    		file = open(new_file_name, 'r')    
    		billnum_lines = 0

    		for line in file:
        		still_happybill.append(line)
        		billnum_lines += 1

		"""doing for olivia"""
		second_file_name = "Olivia" + "friend.txt"
		second_file = open(second_file_name, 'r')
		olivianum_lines = 0
		
		for line in second_file:
			still_happyolivia.append(line)
			olivianum_lines += 1
		

		client = TwilioRestClient(account_sid, auth_token)
                
		for x in (0, 2):
			message = client.messages.create(to="+14103532508", from_="+14437753700", 
					body=still_happybill[random.randint(0, billnum_lines-1)])

		"""send to Olivia"""
		for x in (0, 2):
                        message = client.messages.create(to="+15206098877", from_="+14437753700",
                                        body=still_happyolivia[random.randint(0, olivianum_lines-1)])
			

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
