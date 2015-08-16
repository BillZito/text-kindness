"""
From Twilio https://www.twilio.com/docs/quickstart/python/sms/hello-monkey
should allow us to send replies to texts 
saving as a new thing
"""

from flask import Flask, request, redirect
import twilio.twiml
 

#open and write text to list--should let it throw exception, should let it be personalized based on user
file = open('bill.txt', 'r')
still_happy = []
for line in file:
	still_happy.append(line)

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    for x in (0,4):
        resp.message(still_happy[8])
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
