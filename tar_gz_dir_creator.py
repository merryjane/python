#!/usr/bin/env python

import sys
import os
import tarfile

def creator(src, dst):
	tar = tarfile.open(dst, "w|gz")
	for root, dir, files in os.walk(src):
		for file in files:
			fullpath = os.path.join(root, file)
			tar.add(fullpath)
	tar.close()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage " + "./" + os.path.basename(__file__) + " SRC DST"
	else:
		src = sys.argv[1]
		dst = sys.argv[2]
		creator(src, dst)
