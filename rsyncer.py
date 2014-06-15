#!/usr/bin/env python

import sys
import os
import time
import subprocess

def mover(source, dest):
	rsync = "rsync"
	arguments = "-azv"
	cmd = "%s %s %s %s" % (rsync, arguments, source, dest)

	while True:
		ret = subprocess.call(cmd, shell=True)
		if ret != 0:
			print "resubmitting rsync"
			time.sleep(15)
		else:
			print "rsync was successful"
			sys.exit(0)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage " + "./" + os.path.basename(__file__) + " SRC DST"
	else:
		source = sys.argv[1]
		dest = sys.argv[2]
		mover(source, dest)
