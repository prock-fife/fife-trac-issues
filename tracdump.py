import xmlrpclib 
import json
import pickle
from optparse import OptionParser

REPO = 'fife/'

TRAC_URL="fife.trac.cvsdude.com/engine/login/xmlrpc"

TICKET_FILE = REPO + 'tickets.p'
TICKETS = {}

def dump_tickets(server):
	tickets = {} 
	# dump tickets
	for ticketid in server.ticket.query("max=0"):
		tickets[ticketid] = server.ticket.get(ticketid)
		tickets[ticketid].append(server.ticket.changeLog(ticketid))
		print ticketid

	f = open(TICKET_FILE, 'wb')
	pickle.dump(tickets, f)

def dump_authors():
	f = open(TICKET_FILE, 'rb')
	TICKETS = pickle.load(f)
	f.close()

	f = open(REPO + 'authors.list', 'w')
	for ticketid in TICKETS:
		comments = TICKETS[ticketid][4]
		for comment in comments:
			f.write(comment[1] + '\n')

def dump_lists(server):		
	# dump ticket status
	f = open(REPO + 'status.list', 'w')
	for status in server.ticket.status.getAll(): 
		line = status + '\n'
		f.write(line)

	# dump components
	f = open(REPO + 'components.list', 'w')
	for component in server.ticket.component.getAll(): 
		line = component + '\n'
		f.write(line)

	# dump versions
	f = open(REPO + 'versions.list', 'w')
	for version in server.ticket.version.getAll(): 
		line = version + '\n'
		f.write(line)

	# dump milestones
	f = open(REPO + 'milestones.list', 'w')
	for milestone in server.ticket.milestone.getAll(): 
		line = milestone + '\n'
		f.write(line)

	# dump types
	f = open(REPO + 'types.list', 'w')
	for typ in server.ticket.type.getAll(): 
		line = typ + '\n'
		f.write(line)

	# dump resolutions
	f = open(REPO + 'resolutions.list', 'w')
	for res in server.ticket.resolution.getAll(): 
		line = res + '\n'
		f.write(line)

	# dump priorities
	f = open(REPO + 'priorities.list', 'w')
	for pri in server.ticket.priority.getAll(): 
		line = pri + '\n'
		f.write(line)

	# dump severities
	f = open(REPO + 'severities.list', 'w')
	for sev in server.ticket.severity.getAll(): 
		line = sev + '\n'
		f.write(line)

def main():
	parser = OptionParser()
	parser.add_option("-u", "--user", dest="user")
	parser.add_option("-p", "--password", dest="password")
	(options, args) = parser.parse_args()

	if(options.user and options.password):
		url="http://" + options.user + ":" + options.password + "@" + TRAC_URL
	else:
		url="http://" + TRAC_URL
	
	server = xmlrpclib.ServerProxy(url) 

	dump_lists(server)
	#dump_tickets(server)
	dump_authors()

if __name__ == '__main__':
	main()
