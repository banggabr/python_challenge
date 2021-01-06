import os
import csv

# Path to collect data from resource
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Create lists
candidates = []
vote_count = []
vote_percent = []
vote_total = []

# Start counter at 0
vote_total = 0

with open(election_csv, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next (csvreader)

    for row in csvreader:
        # Add each vote and total 
        vote_total +=1
        
        if row[2] not in candidates: 
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_count.append(1)
        else: 
            index = candidates.index(row[2])
            vote_count[index] += 1

    # Add to vote_percent list
    for votes in vote_count:
        percentage = (votes/vote_count) * 100
        percentage = round(percentage)
        percentage = '%.3f%%' % percentage
        vote_percent.append(percentage)

    # Winning Candidate
    winner = max(vote_count)
    index = vote_count.index(winner)
    winning_candidate = candidates [index]

# Print results
print('Election Results')
print('--------------------------')
print(f'Total Votes: {str(vote_total)}')
print('--------------------------')
for x in range(len(candidates)): 
    print(f'{candidates[x]}: {str(vote_percent[x])} ({str(vote_count[x])})')
print('--------------------------')
print(f'Winner: {winning_candidate}')
print('--------------------------')