"""
my attempt to set up a flask script
"""

from flask import Flask, request, redirect
import twilio.twiml
import random

app = Flask(__name__)

@app.route("/")
def thank_bill():
	print "bill youre the best"

if __name__ == "__main__":
	app.run(debug=True)

