# python version 2.7
# coding: utf-8
import datetime as dt

class timecounter(object):
	def __init__(self):
		self.startdate = self.now()
		self.date = self.startdate
	
	def now(self):
		return dt.datetime.today()
	
	### between now and before getcol method starting
	def getcol(self):
		n = self.now()
		difscore = n - self.date
		self.date = n
		return difscore
	
	### between now and class making 
	def getall(self):
		n = self.now()
		difscore = n-self.startdate
		return difscore
		

### test method	
if __name__ == "__main__":
	ob = timecounter()
	print ob.getcol()
	print ob.getall()
	print ob.getcol()
	print ob.getall()
