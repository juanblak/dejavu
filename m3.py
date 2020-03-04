import warnings
import json
import os
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

	# create a Dejavu instance
	djv = Dejavu(config)
	# Recognize audio from a file
	testdir="test_reaction"
	# testdir = "test_fancam"
	rc=0 # can detect
	nc=0 # can't detect
	yc=0 # right result
	wc=0 # wrong result
	for root, dirs, testfiles in os.walk(testdir):
		for filename in testfiles:
			song= djv.recognize(FileRecognizer, testdir+"/"+filename)
			if song == None: #can't detect
				print filename,song
				nc+= 1
				continue

			result=song['song_name']
			rc+=1 # can detect

			if result[:2] == filename[:2]:
				print "yes", filename
				yc+=1 # right result
			else:
				wc+=1 # wrong result
				print "no" ,filename,song['song_name']


	# acc=yc*1.0/(yc+wc)
	det_rate=(rc-wc)*1.0/(nc+rc)
	inc_rate=wc*1.0/rc
	print "result:%d  none:%d  right:%d  wrong:%d  detction rate=:%.2f  inccorect_rate=:%.2f" % (rc,nc,yc,wc,det_rate*100,inc_rate*100)
