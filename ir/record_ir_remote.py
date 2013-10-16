import RPi.GPIO as GPIO
import pylirc, time

class IRRecorder:
	def __init__(self):
		#if pylirc.init("../lirc.conf") == 0:
		#	print "IRRecorder::failed to initialize."
		GPIO.setup(16, GPIO.IN)
		pass
	def startRecord(self):
		code = pylirc.nextcode()

		if code == None:
			return

		print code

	def test(self):
		blocking = 0;

		#
		if(pylirc.init("pylirc", "./conf", blocking)):

		   code = {"config" : ""}
		   while(code["config"] != "quit"):

		      # Very intuitive indeed
		      if(not blocking):
			 print "."

			 # Delay...
			 time.sleep(1)

		      # Read next code
		      s = pylirc.nextcode(1)

		      # Loop as long as there are more on the queue
		      # (dont want to wait a second if the user pressed many buttons...)
		      while(s):
			 
			 # Print all the configs...
			 for (code) in s:
			 
			    print "Command: %s, Repeat: %d" % (code["config"], code["repeat"])
			    
			    if(code["config"] == "blocking"):
			       blocking = 1
			       pylirc.blocking(1)

			    elif(code["config"] == "nonblocking"):
			       blocking = 0
			       pylirc.blocking(0)

			 # Read next code?
			 if(not blocking):
			    s = pylirc.nextcode(1)
			 else:
			    s = []

		   # Clean up lirc
		   pylirc.exit()


irr = IRRecorder()

irr.test()
