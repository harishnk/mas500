######################################
#
#change history
#hnk_mas500: Modifications for MAS500
#
######################################

import collections

class ElectionResults:
  
  def __init__(self, filename):
    self.filename = filename

  def load(self):
    self.file = open(self.filename, 'r')
    self.all_lines = self.file.readlines()[1:] #hnk_mas500 skip first line

  def states(self):
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      all_names.append(columns[1])
    return all_names

  def state_count(self):
    return len(self.all_lines)

  # begin of hnk_mas500+{
  def candidate_count(self):
    """Counts the total votes for Obama(C1) and Romney(C2)
        Returns a named tuple:
            Totalvotes('Totalvotes', 'C1votes, C2votes')
    """
    all_c1_votes = []
    all_c2_votes = []
    for line in self.all_lines:
        columns = line.split(',')
        all_c1_votes.append(float(columns[3]))
        all_c2_votes.append(float(columns[5]))
    Totalvotes = collections.namedtuple('Totalvotes', 'C1votes, C2votes')
    totalvotes = Totalvotes(sum(all_c1_votes), sum(all_c2_votes))
    #totalvotes(sum(all_obama_votes), sum(all_romney_votes))
    return totalvotes

  @staticmethod
  def evaluate_winner(c1votes, c2votes):
    """Compares c1votes and c2votes
           Returns 1 if c1 wins, 2 if c2 wins, 0 if tie
    """
    if c1votes > c2votes:
        return 1
    elif c2votes < c1votes:
        return 2
    else:
        return 0
  # end of hnk_mas500+}  



