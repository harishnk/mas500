from electiondata import ElectionResults

import unittest

class ElectionResultsTest(unittest.TestCase):

	def setup(self):
		self.results = ElectionResults('/Users/harishnk/mas500/Programming-Style-Examples/election_results_test_file.csv')
		assert self.results!=None

	def testload(self):
		self.results.load()
		assert self.results!=None
		assert self.results.file!=None

	def testStateCount(self):
		self.results.load()
		state_count = self.results.state_count()
		assert state_count>=2

	def testStates(self):
		self.results.load()
		all_names = []
		all_names = self.results.states()
		assert len(all_names)==2
		assert all_names[0]=='Alaska'
		assert all_names[1]=='Alabama'

	def testCandidateCount(self):
		self.results.load()
		totalvotes = self.candidate_count()
		assert totalvotes.C1votes==885316
		assert totalvotes.C2votes==1373687

	def testEvaluateWinner(self):
		self.results.load()
		totalvotes = self.candidate_count()    
		winner = ElectionResults.evaluate_winner(totalvotes.C1votes, totalvotes.C2votes)
		assert winner==2	    

# if this file is run directly, run the tests
if __name__ == "__main__":
	unittest.main()    