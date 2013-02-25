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
