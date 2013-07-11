#!/usr/bin/env python

import base64
import sys
import getopt
def Usage():
	print "\tCrack.py Usage:"
	print "\t-h,--help: print help message and exit."
	print "\t-v,--version:print script version."
	print "\t-e,--encode:encode the url."
	print "\t-d,--decode:decode the url."
	print "\t-t,--thunder:use thunder to encode or decode."
	print "\t-q:use qql."
	print "\t-f:use flashget."
def Version():
	print "Crack.py 0.0.1"
class Crack(object):
	def __init__(self,src_url=None):
		if not src_url:
			print "fuck."
			sys.exit(2)
		self.src=src_url
	def get_thunder_decode(self):
		return base64.b64decode(self.src[10:])[2:-2]
	def get_thunder_encode(self):
		return  "thunder://%s"%base64.b64encode("AA%sZZ"%self.src)
	def get_flashget_decode(self):
		return base64.b64decode(self.src[11:-1])[10:-10]
	def get_flashget_encode(self):
		url="[FLASHGET]%s[FLASHGET]"%self.src
		return "flashget://%s&"%base64.b64encode(url)
	def get_QQ_downl_decode(self):
		return base64.b64decode(self.src[7:])
	def get_QQ_downl_encode(self):
		return "qqdl://%s"%base64.b64decode(self.src)
def main(argv):
	try:
		opts,args=getopt.getopt(argv[1:], shortopts="hvedt:q:f:",longopts=['help','version'])
	except getopt.GetoptError,err:
		print str(err)
		Usage()
		sys.exit(2)
	if not opts:
		Usage()
		sys.exit(2)
	decode=True
	for o,a in opts:
		if o in ('-h','--help'):
			Usage()
			sys.exit(0)
		elif o in ('-v','--version'):
			Version()
			sys.exit(0)
		elif o in ('-e','-d'):
			if o=='-e':
				decode=False
		elif o in ('-t','-q','-f'):
			obj=Crack(a)
			if decode:
				if o=='-t':
					print obj.get_thunder_decode()
				elif o=='-q':
					print obj.get_QQ_downl_decode()
				else:
					print obj.get_flashget_decode()
			else:
				if o=='-t':
					print obj.get_thunder_encode()
				elif o=='-q':
					print obj.get_QQ_downl_encode()
				else:
					print obj.get_flashget_encode()
		else:
			print 'Error.Unabled to parser.'
			sys.exit(1)

if __name__=="__main__":
	main(sys.argv)
