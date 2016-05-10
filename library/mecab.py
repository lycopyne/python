# python version 2.7
# -*- coding:utf-8 -*-
"""
    ana(text)：string[](string)
        形態素解析
    anan(text, noun)：string[](string, string)
        品詞を絞った形態素解析
    anadata(text)：
    test：サンプル
    test2：サンプル２
    main：サンプル
"""
import MeCab
import sys

### Constants
mecabmode = 'mecabrc'
tagger = MeCab.Tagger(mecabmode)
class mecab:
	@staticmethod
	def ana(text):
		node = tagger.parseToNode(text)
		data = []
		print node
		while node:
			word = node.surface
			if word == '':
				node = node.next
				continue
			print word
			#data.append(word.decode('utf-8'))
			data.append(word)
			node = node.next
		return data
	
	@staticmethod
	def anan(text, noun):
		tagger = MeCab.Tagger(mecabmode)
		node = tagger.parseToNode(text)
		data = []
		while node:
			nouns = node.feature
			word = node.surface
			nounlist = nouns.split(',')
			appnoun = noun.split(',')
			if len(appnoun) == 1:
				appnoun = noun
			ans = True
			for hoge in range(len(appnoun)):
				if nounlist[hoge] != appnoun[hoge]:
					ans = False
			if ans == True:
				data.append(word)
			node = node.next
		return data
		
	@staticmethod
	def anadata(text):
		node = MeCab.Tagger(" ".join(sys.argv)).parseToNode(text)
		return node

	@staticmethod
	def test():
		try:
			sentence = '今日は良い天気だったなぁ(感想)'
			t = MeCab.Tagger(" ".join(sys.argv))
			print t.parse(sentence)
			m = t.parseToNode(sentence)
			while m:
				print m.surface, "\t", m.feature
				m = m.next
			print "EOS"
			
			lattice = MeCab.Lattice()
			t.parse(lattice)
			lattice.set_sentence(sentence)
			leng = lattice.size()
			for i in range(leng + 1):
				b = lattice.begin_nodes(i)
				e = lattice.end_nodes(i)
			while b:
				print "B[%d] %s\t%s" % (i, b.surface, b.feature)
				b = b.bnext 
			while e:
				print "E[%d] %s\t%s" % (i, e.surface, e.feature)
				e = e.bnext 
			print "EOSS"
			
			d = t.dictionary_info()
			while d:
				print d.filename
				print d.charset
				print d.size
				print d.type
				print d.lsize
				print d.rsize
				print d.version
				d = d.next
		except RuntimeError, e:
			print "RuntimeError : ", e
			
	@staticmethod
	def test2(text):
		t = MeCab.Tagger('-Owakati')
		result = t.parse(text)
		res = result.split(' ')
		print result
		counter = 0
		for i in res:
			j = i.decode("utf-8")
			res[counter] = j
			print '{0}\t{1}' .format(i, j)
			counter += 1
		return res


if __name__ == "__main__":
	#text = u'today is a beautiful day'
	#mecab.analy(text)
	#ob = mecab
	data = mecab.ana(sentence)
	for i in data:
		print i
	tester = []
	for i in range(20):
		tester.append('{0}'.format(i))
	print data
	print tester
	#print mecab.anan(sentence, '名詞')
	
	
    