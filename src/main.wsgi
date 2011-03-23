#!/usr/bin/python

#from fast import app as application

#def application(environ, start_response):
#	status='200 OK'
#	output = 'Hello world'

#	response_headers = [('Content-type', 'text/plain'),  ('Content-Length', str(len(output)))]  
#	start_response(status, response_headers)  

#	return output

import sys
sys.path.append("/home/conan/workspace/app/DotABook/src")

from dota import app
application = app
