from flask import Flask, request, redirect
from flask.ext.script import Manager
from flask.ext.script import Command
from twilio.rest import TwilioRestClient

app = Flask(__name__)

manager = Manager(app)
 
account_sid = "AC391d717b317d85ec6bc4278575769ab2"
auth_token = "e306bcddeef2de9a43a7fac69c835eec"

class Send(Command):
	"send a message to myself"
	
	def run(self):
		client = TwilioRestClient(account_sid, auth_token)
 		message = client.messages.create(to="+14103532508", from_="+14437753700",
                                     body="Hello there!")

class Hello(Command):
        "prints hello world"

        def run(self):
                print "bill is a boss"


manager.add_command('hello', Hello())
manager.add_command('send', Send())

if __name__ == "__main__":
	manager.run()
