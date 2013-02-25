#!/usr/bin/env python2
# The MIT License (MIT)
#
# Copyright (c) 2013 Wayne Prasek <wprasek@gmail.com>
# based on work Copyright (c) 2012 Chris Oelmueller <chris.oelmueller@gmail.com>
# based on work Copyright (c) 2010 Thomas Adamcik
#
# Permission is hereby granted, free of charge,  to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction,  including without limitation the rights
# to use,  copy, modify,  merge, publish,  distribute, sublicense,  and/or sell
# copies of the Software,  and to permit persons  to whom  the Software is fur-
# nished to do so, subject to the following conditions:
#
# The above  copyright notice  and this permission notice  shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS  PROVIDED "AS IS",  WITHOUT WARRANTY OF ANY KIND,  EXPRESS OR
# IMPLIED,  INCLUDING  BUT NOT  LIMITED TO  THE WARRANTIES  OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR  PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR  COPYRIGHT HOLDERS  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIA-
# BILITY,  WHETHER IN AN ACTION OF CONTRACT,  TORT OR OTHERWISE,  ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import xmlrpclib 
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-u","--user",dest="user")
parser.add_option("-p","--pasword",dest="password")

(options, args) = parser.parse_args()

if (options.user and options.password):
	url="http://" + options.user + ":" + options.password + "@fife.trac.cvsdude.com/engine/login/xmlrpc"
else:
	print "Specify a username and password!"
	sys.exit(1)
	 
server = xmlrpclib.ServerProxy(url) 
for method in server.system.listMethods(): 
	print method 
	print '\n'.join(['  ' + x for x in server.system.methodHelp(method).split('\n')]) 
	print 
	print 
