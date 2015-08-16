"""
From Twilio https://www.twilio.com/docs/quickstart/python/sms/hello-monkey
should allow us to send replies to texts 
saving as a new thing
"""

from flask import Flask, request, redirect
import twilio.twiml
 

#open and write text to list--should let it throw exception, should let it be personalized based on user
def make_my_list():
	file = open('bill.txt', 'r')
	for line in file:
	        still_happy.append(line)
	return "successsss"

#uses the list to send three random compliments--should let it throw exception
def send_three(email, recepient, message):
	for x in (0,3):
		server.sendmail(email, recepient, still_happy[random.randint(1,190)]) 
	return "three messages sent"

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    for x in (0,3):
        resp.message("Hello, Mobile Monkey")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
