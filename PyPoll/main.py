#import modules
import os
import csv

csvPath = os.path.join('/Users/treazkenshin/Downloads/cwru-cle-data-pt-01-2021-u-c-master-Homework-03-Python/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv')
txtPath = os.path.join('/Users/treazkenshin/Downloads/cwru-cle-data-pt-01-2021-u-c-master-Homework-03-Python/Homework/03-Python/Instructions/PyPoll/Resources/election_results.txt')

#Define variables
totalVotes = 0
candidateVotes = {}
winner = None

with open(csvPath) as csvFile:
    
    #CSV reader
    voteData = csv.DictReader(csvFile)

    for row in voteData:
        
        candidate = row['Candidate']
        if candidate not in candidateVotes:
            candidateVotes[candidate] = 0
            
        candidateVotes[candidate] = candidateVotes[candidate] + 1
        
        totalVotes = totalVotes + 1
        
#print(totalVotes)
#print(candidateVotes)

#Find Votes
for candidate in candidateVotes:
    #print(candidate)
    
    votes = candidateVotes[candidate]
    #print(votes)
    
    if winner is None or votes > candidateVotes[winner]:
        winner = candidate
    #print(winner)
    

output = f'''
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
'''
  # Khan: 63.000% (2218231)
  # Correy: 20.000% (704200)
  # Li: 14.000% (492940)
  # O'Tooley: 3.000% (105630)
  # -------------------------
  # Winner: Khan
  # -------------------------
  # ```
  
for candidate in candidateVotes:
      votes = candidateVotes[candidate]
      percentage = votes / totalVotes
      output += candidate+": "+"{:.3f}".format(percentage*100.)+"% ("+str(votes)+")\n"
      
output += f'''-------------------------
Winner: {winner}
-------------------------
'''
      
print(output)
with open(txtPath, "w") as txtFile:
    txtFile.write (output)

      