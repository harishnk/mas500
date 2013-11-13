#!/usr/bin/python

from electiondata import *

import collections

import json

running_in_prompt = ""

if running_in_prompt == "X":
	filepath = raw_input('Please enter the location of the file--> ')
	electionResults = ElectionResults(filepath)
else:
	electionResults = ElectionResults('/Users/harishnk/mas500/Programming-Style-Examples/2012_US_election_state.csv')
#totalvotes = namedtuple('totalvotes', 'Obamavotes, Romneyvotes')
electionResults.load()
totalvotes = electionResults.candidate_count()
print "election results are: Obama's total votes = %s" % (int(totalvotes.C1votes))
print "                     Romney's total votes = %s" % (int(totalvotes.C2votes))

winner = ElectionResults.evaluate_winner(totalvotes.C1votes, totalvotes.C2votes)
if winner == 0:
	print "It's a tie!"
elif winner == 1:
	print "Obama wins!"
elif winner == 2:
	print "Romney wins!"
else:
	print "Invalid computation. Were the ballots rigged?"

jsonexport = { "Obama votes": int(totalvotes.C1votes),
			   "Romney votes": int(totalvotes.C2votes)
			 }

print json.dumps(jsonexport, indent=4)

