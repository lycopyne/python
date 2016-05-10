# python version 2.7
# coding: utf-8
import numpy as np
import math as math

class encoder(object):
	def __init__(self, w_path, ebias_path):
		self.W = self.makematrix(w_path)
		self.Ebias = self.makematrix(ebias_path)
		if len(self.W) != len(self.Ebias):
			print '\t encode length not match : w{0} : ebias{1}' .format(len(self.W), len(self.Ebias))
	
	### encode file data
	def encfile(self, readpath):
		print '{0} encoding・・・' .format(readpath)
		linecount = 0
		### make write file name
		writepath = readpath.replace('.txt', '')
		number = 1
		if '_h' in writepath:
			spl = writepath.split('_h')
			spli = spl[1].split('_')
			number = int(spli[0]) + 1
			writepath = spl[0]
		writepath = writepath  + '_h' + str(number)
		writepath = writepath + '_' + str(len(self.W[0])) + 'to' + str(len(self.W)) + '.txt'
		
		fw = open(writepath, 'w')
		for line in open(readpath, 'r'):
			sp = line.rstrip().split('\t')
			if(len(self.W[0]) != (len(sp)-1)):
				print 'length not match \'vector_length\' and \'line_length\' : v {0} : line {1}' .format(self.vl, len(sp)-1)
			x = []
			if len(sp) == 0:
				print 'this file not match logisticregression.py : {0}' .format(path)
			### write label
			fw.write(sp[0])
			leng = 1
			### write vector
			while leng < len(sp):
				x.append(float(sp[leng]))
				leng += 1
			#y = self.enc(x)
			y = self.enc(np.array([x]))
			for i in range(len(y)):
				for j in range(len(y[i])):
					fw.write('\t')
					fw.write(str(y[i][j]))
			fw.write('\n')
			linecount += 1
		fw.close()	
	
	### encode
	### double = enc(np.array([]))
	def enc(self, x):
		y = self.W.dot(x.transpose())+self.Ebias
		y = self.sigmoid(y)
		return y
		
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
	
	### make data matrix
	### np.array() = datachange()
	def makematrix(self, filepath):
		data = []
		for line in open(filepath, 'r'):
			line = line.rstrip()			
			sp = line.split('\t')
			d = []
			for now in range(len(sp)):
				d.append(float(sp[now]))
			data.append(d)
		return np.array(data)		

if __name__ == "__main__":
	print 'encode start'
	w_path = 'encoder_learn/h1_814to400_w.txt'
	bias_path = 'encoder_learn/h1_814to400_eb.txt'
	readpath = 'encoder_test.txt'
	ob = encoder(w_path, bias_path)
	ob.encfile(readpath)
	print 'finish'