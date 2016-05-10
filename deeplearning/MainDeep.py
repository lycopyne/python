# python version 2.7
# coding: utf-8
import numpy
from autoencoder import autoencoder
from encoder import encoder

if __name__ == "__main__":
	### autoencoder parameter
	iteration = 100
	learning = 0.005
	x_length = 1000
	y_length = 100
	prob = 0.0
	filepath = 'lr.txt'
	w_path = 'lr/h1_1000to100_w.txt'
	bias_path = 'lr/h1_1000to100_eb.txt'
	readpath1 = 'lr.txt'
	readpath2 = 'lt.txt'
	### stacked denoising autoencoder
	print 'sda start'
	ob1 = autoencoder(iteration, learning, x_length, y_length, filepath, prob)
	ob1.sda()
	ob1.encfile(readpath1)
	ob1.encfile(readpath2)
	print 'autoencoder finish'
	
"""
	print 'encode start'
	ob2 = encoder(w_path, bias_path)
	ob2.encfile(readpath1)
	ob2.encfile(readpath2)
	print 'finish'
"""