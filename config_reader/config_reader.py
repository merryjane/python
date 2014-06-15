#!/usr/bin/env python

import subprocess
import ConfigParser

def readConfig(file="config.ini"):
	ips = []
	cmds = []

	Config = ConfigParser.ConfigParser()
	Config.read(file)

	machines = Config.items("MACHINES")
	commands = Config.items("COMMANDS")

	# Example output of Config.items("MACHINES")
	# print machines
	# [('centos', '10.0.1.40'), ('ubuntu', '10.0.1.50'), ('redhat', '10.0.1.51'), ('sun', '10.0.1.60'), ('freebsd', '10.0.1.80')]

	for ip in machines:
		ips.append(ip[1])
	for cmd in commands:
		cmds.append(cmd[1])
	
	return ips, cmds

if __name__ == '__main__':
	print readConfig()
'''
	ips, cmds = readConfig()
	for ip in ips:
		for cmd in cmds:
			subprocess.call("ssh root@%s %s" % (ip, cmd), shell=True)
'''
