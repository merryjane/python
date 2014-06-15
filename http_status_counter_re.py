#!/usr/bin/env python

import sys
import os
import re

log_line_re = re.compile(r'''(?P<remote_host>\S+)
				\s+
				(?P<request_time>\S+)
				\s+
				(?P<host>\S+)
				\s+
				\S*
				\s*
				\[[^\[\]]+\]
				\s+
				"[^"]+"
				\s+
				(?P<status>\d+)
				\s+
				(?P<body_bytes_sent>-|\d+)
				\s+
				(?P<http_referer>\S+)
				\s+
				(?P<http_user_agent>\S+)
				\s*
				''', re.VERBOSE)
def dictify_log(line):
	m = log_line_re.match(line)
	if m:
		groupdict = m.groupdict()
		return groupdict
	else:
		return "WTF in regexp!"
	
def status_counter(file):
	status_200 = 0
	status_301 = 0
	status_302 = 0 
	status_403 = 0
	status_404 = 0
	status_500 = 0
	status_502 = 0
	status_503 = 0
	status_504 = 0
	status_other = 0

	for line in file:
		string_for_parse = dictify_log(line)
		try:
			if int(string_for_parse['status']) == 200:
				status_200 += 1
			elif int(string_for_parse['status']) == 301:
				status_301 += 1
			elif int(string_for_parse['status']) == 302:
                	        status_302 += 1
			elif int(string_for_parse['status']) == 403:
				status_403 += 1
			elif int(string_for_parse['status']) == 404:
				status_404 += 1
			elif int(string_for_parse['status']) == 500:
				status_500 += 1
			elif int(string_for_parse['status']) == 502:
				status_502 += 1
			elif int(string_for_parse['status']) == 503:
				status_503 += 1
			elif int(string_for_parse['status']) == 504:
				status_504 += 1
			else:	status_other += 1
		except ValueError:
			continue
	
	return {'status_200': status_200,
		'status_301': status_301,
		'status_302': status_302,
		'status_404': status_404,
		'status_500': status_500,
		'status_502': status_502,
		'status_503': status_503,
		'status_504': status_504,
		'status_other': status_other,
		
	}

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Usage " + "./" + os.path.basename(__file__) + " LOG_FILE"
	else:
		in_file_name = sys.argv[1]
		with open(in_file_name, 'r') as in_file:
			print status_counter(in_file)
