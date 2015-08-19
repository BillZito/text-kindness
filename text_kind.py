"""
lots copied from Twilio https://www.twilio.com/docs/quickstart/python/sms/hello-monkey
allows user to receive their own message responses 
"""

from flask import Flask, request, redirect
import twilio.twiml
import random 


app = Flask(__name__)

#list of numbers to look up upon receiving message
callers = {
    "+14158675309": "Curious George",
    "+14103532508": "BillZ",
    "+14109910925": "Mellie",
    "+14432547513": "BillC",
    "+15206098877": "Olivia",
    "+13019436377": "Hannah",
    "+14138414718": "Alice",
    "+14103530094": "Jenny",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming messages with three messages from their list"""
    
    #identify their number
    from_number = request.values.get('From', None)
    
    #if number in our directory above, pick out their name and add it to message string to be sent below
    if from_number in callers:
        message = callers[from_number]
    
    #otherwise, consider them a monkey and respond accordingly
    else:
        message = "Monkey" 


    #open and write text to list--should let it throw exception, should let it be personalized based on user
    #initalize list
    still_happy = []
    
    #initalize file and then fill the list with the file contents
    new_file_name = message + ".txt"
    file = open(new_file_name, 'r')    
    num_lines = 0
    for line in file:
        still_happy.append(line)
        num_lines += 1

    #make a new instance of a twiml response
    resp = twilio.twiml.Response()

    #send three messages through said instance
    for x in (0,2):
        resp.message(still_happy[random.randint(0, num_lines-1)])

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
