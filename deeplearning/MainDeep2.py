# python version 2.7
# coding: utf-8
import numpy
from autoencoder import autoencoder
from encoder import encoder

if __name__ == "__main__":
	### autoencoder parameter
	print '\t iteration : (100 or 1000)'
	ite = raw_input()
	iteration = int(ite)
	print '\t learning prob : (0.1 or 0.05)'
	lp = raw_input()
	learning = float(lp)
	x_length = 400
	print '\t y_length : (50 ~ 600)'
	yl = raw_input()
	y_length = int(yl)
	print '\t noise prob : (0.05 ~ 0.3)'
	p = raw_input()
	prob = float(p)
	filepath = 'el.txt'
	w_path = 'el/h1_400to'+yl+'_w.txt'
	bias_path = 'el/h1_400to'+yl+'_eb.txt'
	readpath1 = 'el.txt'
	readpath2 = 'et.txt'
	### stacked denoising autoencoder
	print 'sda start'
	ob1 = autoencoder(iteration, learning, x_length, y_length, filepath, prob)
	ob1.sda()
	print 'autoencoder finish'
	
	print 'encode start'
	ob2 = encoder(w_path, bias_path)
	ob2.encfile(readpath1)
	ob2.encfile(readpath2)
	print 'finish'
	