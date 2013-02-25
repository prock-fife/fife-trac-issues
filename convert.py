#!/usr/bin/env python2
# The MIT License (MIT)
#
# Copyright (c) 2012 Chris Oelmueller <chris.oelmueller@gmail.com>
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
COMMENTS_PATH = REPO + 'issues/%s.comments.json'
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
    return t or 'Empty!' # No empty issue bodies are supported

def github_label(text):
    """If you do not like the idea of having all your labels converted to
    lower case, now would be a great opportunity to edit one line of code.
    """
    return unicode(text.lower())

def github_time(date):
    """Takes trac date, returns github-ready timestamp. Yes, trac
    for whatever reason may store dates in a highly weird format.
    Only necessary for comments, the tickets are extracted per web
    and thus do not rely on a date representation in trac's db.
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
            reporter=author) + body
    return {
          'body': body,
          'user': user,
          'created_at': github_time(date),
          }

def write_issue(row, outfile):
    """Dumps a csv line *row* from the issue query to *outfile*.
    """
    for key, value in row.items():
        row[key] = row[key].decode('utf-8')
    # Issue text body
    body = row.get('_description', u'')
    body = trac_to_gh(body) + '\r\n\r\n' \
        '[> Link to originally reported Trac ticket <] ({url})'.format(
        url=TRAC_TICKET_URL % row['ticket'])

    # Default state: open (no known resolution)
    state = STATES.get(row.get('status'), 'open')

    # Trac will have stored some kind of username.
    reporter = row['_reporter']

    # Not sure whether we have a related github account for that user.
    if USERNAMES.get(reporter):
        userdata = USERNAMES[reporter]
    else: # If we do not, at least mention the user in our issue body
        userdata = DEFAULT_USER
        body = ('This issue was reported by **%s**\r\n\r\n' % reporter) + body

    # Whether this is stored in 'milestone' or '__group__' depends on the
    # query type. Try to find the data or assign the default milestone 0.
    milestone_info = row.get(('milestone'), row.get('__group__'))
    milestone = MILESTONES.get(milestone_info, 0)

    labels = [] # Collect random tags that might serve as labels
    for tag in ('type', 'component', 'priority'):
        if row.get(tag) and LABELS.get(row[tag]):
            label = LABELS[row[tag]]
            labels.append({'name': github_label(label)})

    # Also attach a special label to our starter tasks.
    # Again, please ignore this.
    #if row['ticket'] in easy_tickets:
    #    labels.append({'name': unicode(LABELS.get('start').lower())})

    # Dates
    updated_at = row.get('modified') or row.get('_changetime')
    created_at = row.get('created') or updated_at

    # Now prepare writing all data into the json files
    dct = {
          'title': row['summary'],
          'body': body,
          'state': state,
          'user': userdata,
          'milestone': {'number': milestone},
          'labels': labels,
          'updated_at': updated_at,
          'created_at': created_at,
       }

    # Assigned user in trac and github account of that assignee
    assigned_trac = row.get('owner')
    assigned = USERNAMES.get(assigned_trac)
    # Assigning really does not make sense without github account
    if state == 'open' and assigned:
        dct['assignee'] = assigned

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
        with open(ISSUES_PATH % ticket, 'w') as f:
            json.dump(data, f, indent=5)

    #######################################################################
    # Write the actual ticket data to separate json files (GitHub API v3)
    #######################################################################
#    csv_data = urllib.urlopen(TRAC_REPORT_URL)
#    ticket_data = csv.DictReader(csv_data)
#    for row in ticket_data:
#        if not (row.get('summary') and row.get('ticket')):
#            continue
#        with open(ISSUES_PATH % row['ticket'], 'w') as f:
#            write_issue(row, f)

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

    #######################################################################
    # Since trac supports ticket deletion, the following was a quick hack
    # to obtain the IDs of all tickets that no longer exist. We used that
    # list to rename existing GH issues to numbers from this pool.
    # All pull requests have an issue ID attached, so you may have issues
    # in your otherwise empty repository without realizing this!
    # Best check with your awesome github go-to if you are not sure.
    #######################################################################
    #ticketnumbers = csv.reader(open('ticket-ids.csv', 'rb'),
    #                           delimiter=CSVDELIM, quotechar=CSVESCAPE)
    #t_ids = set([int(t[0]) for t in ticketnumbers])
    #available_ids = [i for i in range(1, max(t_ids)) if i not in t_ids]
    #print len(available_ids), max(t_ids) + 1,  sorted(available_ids)
    #######################################################################

if __name__ == '__main__':
    main()
