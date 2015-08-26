from flask.ext.script import Command

class Hello(Command):
	"prints hello world"
	
	def run(self):
		print "hello world"

