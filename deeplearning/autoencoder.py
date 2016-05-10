# python version 2.7
# coding: utf-8
import numpy as np
import math as math
import os as f
						
class autoencoder(object):
	def __init__(self, iteration, learning, x_length, y_length, filepath, prob):
		### iteration number
		self.iteration = iteration
		### first learning probably
		self.learning = learning				
		### input vector length
		self.x_length = x_length			
		### hidden layer vector length (when encode length)
		self.y_length = y_length
		### learning file path
		self.filepath = filepath
		### noising probably (lost data probably)
		self.prob = prob
		
		### hidden layer transformation matrix (x*y matrix)
		### W[y][x]
		self.W = np.random.RandomState(1111).rand(self.y_length, self.x_length)
		### when encode bias
		self.Ebias = np.random.RandomState(2222).rand(self.y_length, 1)
		### when decode bias
		self.Dbias = np.random.RandomState(3333).rand(self.x_length, 1)
		### record cross entropy error function (JP : 交差エントロピー誤差関数)
		self.ceeflist = []
		### random
		self.rd = np.random.RandomState(4444)

	### main method - Stacked Denoising Autoencoder
	### sda()
	def sda(self):
		print '{0} autoencoding・・・' .format(self.filepath)
		data = self.datachange()
		linecount = 0
		for ite in range(self.iteration):				
			### cross entropy error function (JP : 交差エントロピー誤差関数)
			ceef = 0.0
			for now in range(len(data)):	
				x = np.array([data[now]]).transpose()
				ytest = self.W.dot(x) + self.Ebias
				y = self.sigmoid(self.W.dot(x)+self.Ebias)
				z = self.sigmoid(self.W.transpose().dot(y) +self.Dbias)	
				xz = x-z
				one = np.array([[1]]*self.y_length)
				temp = self.W.dot(xz)*y*(one-y)
				self.W = self.W + self.learning*(temp.dot(x.transpose()) + xz.dot(y.transpose()).transpose())		
				self.Ebias = self.Ebias + self.learning*temp		
				self.Dbias = self.Dbias + self.learning*xz		
				ceef = ceef + self.entropy(x, z)
			### renewal check
			if linecount % 5 == 0:
				print ' ■ ■ ■ {0} iteration ■ ■ ■ ' .format(ite)			
				print '\t L(θ) = {0}' .format(ceef)
				print '\t{0}\t{1}\t{2}' .format(self.W[0][0], self.W[0][1], self.W[0][2])
			self.ceeflist.append(ceef)
			self.learning = self.learning * 0.95
			linecount += 1
		self.writedata()
						
	### cross entropy error function calculation matrix (return double)					
	### double = entropy(double[], double[])
	def entropy(self, x, z):
		score = 0.0 
		for hoge in range(len(x)):				
			score = score + self.ent(x[hoge], z[hoge])			
		return score
		
	### cross entropy error function calculation				
	### L(θ) = (-x * Log(z)) - ((1-x) * Log(1-z))					
	### double = ent(double, double)					
	def ent(self, x, z):
		if z == 0.0 or z == 1.0:
			return 0.0
		return -x*math.log(z)  - (1-x)*math.log(1-z)
	
	### noising matrix x
	### np.array() = noising(np.array())
	def noising(self, x):
		noise = np.array(x)			
		for i in range(len(x)):
			for j in range(len(x[i])):
				if rd.random() < self.prob:
					noise[i][j] = 0.0
		return noise

	### sigmoid matrix
	### np.array() = sigmoid(np.array())
	def sigmoid(self, x):
		score = x
		for i in range(len(x)):
			for j in range(len(x[i])):
				score[i][j] = self.sig(x[i][j])
		return score
	
	### sigmoid function (over large or small : approximation)
	### double = sigmoid(double)
	def sig(self, x):
		if x > 100:
			return 1
		elif x < -100:
			return 0
		return 1.0 / (1.0 + math.exp(-x))
						
	### write [ hidden layer data ] and [ cross entropy error function ] file
	### writedata()
	def writedata(self):
		### make write file name
		directory = self.filepath.replace('.txt', '/')
		if f.path.exists(directory) == False:
			f.mkdir(directory)
		number = 1
		if '_h' in self.filepath:
			spl = self.filepath.split('_h')
			spli = spl[1].split('_')
			number = int(spli[0]) + 1
		name = directory + 'h' + str(number) + '_'
		name = name + str(self.x_length) + 'to' + str(self.y_length) + '_'
		wname =name + 'w.txt'
		ebname = name + 'eb.txt'
		dbname = name + 'db.txt'
		ceefname = name + 'ceef.txt'

		fw = open(wname, 'w')				
		for row in self.W:				
			writetext = ''			
			for col in row:			
				writetext = writetext + str(col) + "\t"		
			writetext = writetext.rstrip()			
			fw.write(writetext + '\n')			
		fw.close()				
		fe = open(ebname, 'w')				
		for row in self.Ebias:
			writetext = ''			
			for col in row:			
				writetext = writetext + str(col) + "\t"		
			writetext = writetext.rstrip()			
			fe.write(writetext + '\n')			
		fe.close()				
		fd = open(dbname, 'w')				
		for row in self.Dbias:
			writetext = ''
			for col in row:			
				writetext = writetext + str(col) + "\t"		
			writetext = writetext.rstrip()			
			fd.write(writetext + '\n')			
		fd.close()
		fc = open(ceefname, 'w')				
		for row in self.ceeflist:
			writetext = ''			
			for col in row:			
				writetext = writetext + str(col) + "\t"		
			writetext = writetext.rstrip()			
			fc.write(writetext + '\n')			
		fc.close()
	
	### make data matrix
	### np.array() = datachange()
	def datachange(self):			
		data = []				
		linecount = 0				
		for line in open(self.filepath, 'r'):	
			line = line.rstrip()			
			sp = line.split('\t')			
			if(self.x_length != (len(sp)-1)):
				print 'x_length not match line_length : x {0} : line{1}, {2}' .format(self.x_length, linecount, len(sp))		
			leng = 1			
			d = []
			while leng < len(sp):			
				d.append(float(sp[leng]))		
				leng = leng + 1		
			data.append(d)			
			linecount = linecount + 1	
		return np.array(data)				

### sample code
if __name__ == "__main__":
	print 'sda start'
	iteration = 100
	learning = 0.01
	x_length = 814
	y_length = 400
	prob = 0.2
	### autoencoderにかけるファイルパス					
	filepath = 'encoder_learn.txt'
	ob = autoencoder(iteration, learning, x_length, y_length, filepath, prob)
	ob.sda()
	print 'finish'				