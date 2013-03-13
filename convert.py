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

import collections
import csv
import datetime
from DateTime import DateTime
import json
import urllib
import pickle 

from data import DEFAULT_USER, USERNAMES, MILESTONES, STATES, LABELS

#######################################################################
# Configuration. Who doesn't like configuration.
#######################################################################
# Your repository name (the subdirectory we will write data to).
REPO = 'fife/'
# Locations of particular files. It is recommended to keep issues
# and comments  in the same directory, which usually is issues/.
ISSUES_PATH = REPO + 'issues/%s.json'
COMMENTS_PATH = REPO + 'issues/%s.%s.comments.json'
MILESTONES_PATH = REPO + 'milestones/%s.json'
# Path to the ticket pickle file
TICKET_FILE = REPO + 'tickets.p'
#
# Magic report id we used to attach special labels to certain tickets
# As all EASY_ stuff, commented out but we used it just like that.
#EASY_NO = 14
#

def trac_to_gh(text):
    """Right, fun goes here. If you aspire to write magic syntax conversion
    from trac to github flavored markdown, this is your place to be. We just
    replaced basic markup because even getting the links right was a headache.
    """
    t = text.replace('}}}', '```')
    t = t.replace('{{{', '```')
    t = t.replace('[[BR]]', '\n')
    return t or '.' # No empty issue bodies are supported

def github_label(text):
    """If you do not like the idea of having all your labels converted to
    lower case, now would be a great opportunity to edit one line of code.
    """
    return unicode(text.lower())

def github_time(date):
    """Takes trac date, returns github-ready timestamp.
    """
    time = DateTime(str(date))
    return time.ISO8601()

def massage_comment(ticket, date, author, body):
    """Expands the ticket comment list for *ticket* with a json comment
    representation of *date*, *author* (mapped to github) and text *body*.
    """
    body = trac_to_gh(body)

    # Not sure whether we have a related github account for that user.
    if USERNAMES.get(author):
        user = USERNAMES[author]
    else: # If we do not, at least mention the user in our comment body
        user = DEFAULT_USER
    
    body = 'This comment was posted by **{reporter}**\r\n\r\n'.format(
            reporter=author) + body + "\r\n\r\n" + github_time(date)

    return {
          'body': body,
          'user': user,
          'created_at': github_time(date),
          }

def write_issue(ticket, outfile):
    """Dumps a csv line *row* from the issue query to *outfile*.
    """
    # Issue text body
    body = ticket[3]['description']
    body = trac_to_gh(body)

    # Default state: open (no known resolution)
    state = STATES.get(ticket[3]['status'], 'open')

    # Trac will have stored some kind of username.
    reporter = ticket[3]['reporter']

    # Not sure whether we have a related github account for that user.
    if USERNAMES.get(reporter):
        userdata = USERNAMES[reporter]
    else: # If we do not, at least mention the user in our issue body
        userdata = DEFAULT_USER
    
    body = ('This issue was reported by **%s**\r\n\r\n' % reporter) + body

    # Whether this is stored in 'milestone' or '__group__' depends on the
    # query type. Try to find the data or assign the default milestone 0.
    milestone_info = ticket[3]['milestone']
    milestone = MILESTONES.get(milestone_info, 3)

    labels = [] # Collect random tags that might serve as labels
    for tag in ('type', 'component', 'priority'):
        if ticket[3].get(tag) and LABELS.get(ticket[3][tag]):
            label = LABELS[ticket[3][tag]]
            labels.append({'name': github_label(label)})


    # Dates
    updated_at = DateTime(str(ticket[2])).ISO8601()
    created_at = DateTime(str(ticket[1])).ISO8601()
    
    # Now prepare writing all data into the json files
    dct = {
          'title': ticket[3]['summary'],
          'body': body,
          'state': state,
          'user': userdata,
          'milestone': int(milestone),
          'labels': labels,
          'updated_at': updated_at,
          'created_at': created_at,
       }

    # Assigned user in trac and github account of that assignee
#    assigned_trac = ticket[3]['owner']
#    assigned = USERNAMES.get(assigned_trac)
    # Assigning really does not make sense without github account
#    if state == 'open' and assigned and assigned['login'] != 'fifengine':
#        print assigned
#        dct['assignee'] = assigned

    # Everything collected, write the json file
    json.dump(dct, outfile, indent=5)

def main():
    #######################################################################
    # Gather information about our tickets (mainly assembles comment list)
    #######################################################################
    # Stores a list of comments for each ticket by ID

    #prock - load pickle file here and generate a row
    f = open(TICKET_FILE, 'rb')
    tickets = pickle.load(f)
    f.close()

    comment_coll = collections.defaultdict(list)

    for ticketid in tickets:
        comments = tickets[ticketid][4]
        for comment in comments:
            if ("comment" in comment):
                dct = massage_comment(ticketid, comment[0],comment[1],comment[4])
                comment_coll[ticketid].append(dct)

    #######################################################################
    # Write the ticket comments to json files indicating their parent issue
    #######################################################################
    for ticket, data in comment_coll.iteritems():
        if (comment_coll[ticket][0]['body'] != '.'):
            count = 0
            for row in data:
                with open(COMMENTS_PATH % (ticket,count), 'w') as f:
                    json.dump(row, f, indent=5)
                    count = count + 1

    #######################################################################
    # Write the actual ticket data to separate json files (GitHub API v3)
    #######################################################################
    for ticketid in tickets:
        with open(ISSUES_PATH % str(ticketid), 'w') as f:
            write_issue(tickets[ticketid], f)

    #######################################################################
    # Finally, dump all milestones and the related data. This script is not
    # attempting to extract due dates or other data. We just manually mined
    # the milestone names once and stored that in MILESTONES for reference.
    #######################################################################
    for name, id in MILESTONES.iteritems():
        with open(MILESTONES_PATH % id, 'w') as f:
            dct = {
                'number': id,
                'creator': DEFAULT_USER,
                'title': name,
            }
            json.dump(dct, f, indent=5)

if __name__ == '__main__':
    main()
