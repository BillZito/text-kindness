"""
lots stolen from Twilio https://www.twilio.com/docs/quickstart/python/sms/hello-monkey
allows user to receive their own message responses 
"""

from flask import Flask, request, redirect
import twilio.twiml
import random 


app = Flask(__name__)

#list of numbers to look up upon receiving message
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+14103532508": "Bill",
    "+14109910925": "Mellie",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming messages with three messages from their list"""
    
    #identify their number
    from_number = request.values.get('From', None)
    
    #if number in our directory above, pick out their name and add it to message string to be sent below
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    
    #otherwise, consider them a monkey
    else:
        message = "Monkey, thanks for the message!" 


    #open and write text to list--should let it throw exception, should let it be personalized based on user
    #initalize list
    still_happy = []
    
    #initalize file and then fill the list with the file contents
    file = open('bill.txt', 'r')    
    for line in file:
        still_happy.append(line)


    #make a new instance of a twiml response
    resp = twilio.twiml.Response()

    #send three messages through said instance
    for x in (0,2):
        resp.message(still_happy[random.randint(0,190)] + message)
    resp.message(still_happy[random.randint(0,190)])

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
