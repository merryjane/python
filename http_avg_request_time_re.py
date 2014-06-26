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

def avg_request_time_counter(file):
	wc = 0
	sum_requests_time = 0

	for line in file:
		string_for_parse = dictify_log(line)
		try:
			sum_requests_time += float(string_for_parse['request_time']) 	
			wc += 1
		except ValueError:
			continue
	avg_request_time = sum_requests_time/wc
	return avg_request_time

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Usage " + "./" + os.path.basename(__file__) + " LOG_FILE"
	else:
		in_file_name = sys.argv[1]
		with open(in_file_name, 'r') as in_file:
			print avg_request_time_counter(in_file)
