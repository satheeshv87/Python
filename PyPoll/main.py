import csv

# Declare variables/list
TotalVotes = 0
candidate = []

# open and read csv file
with open(r'C:\Users\sathe\Documents\UTAMCB201904DATA3\03-Python\Homework\Instructions\PyPoll\Resources\election_data.csv', 'r') as csv_file:

    # read csv to get distinct candidate names
    csv_reader = csv.reader(csv_file)
    # skip header
    next(csv_reader)
    
    for eachrow in csv_reader:
        # Get Total
        TotalVotes = TotalVotes + 1

        # Add distinct candidate to candidate list
        if eachrow[2] not in candidate:
            candidate.append(eachrow[2])

    # Get Candidate count and create a empty list based on the candidate count to hold vote counts
    numberofcandidates = len(candidate)
    candidatevotes = [0] * numberofcandidates

    # take cursor from end of file to start of the file   
    csv_file.seek(0)

    # read csv for next to get counts
    csv_reader2 = csv.reader(csv_file)
    next(csv_reader2)

    for row in csv_reader2:
        for i in range(0, numberofcandidates):
            if candidate[i] == row[2]:
                candidatevotes[i] = candidatevotes[i] + 1
                i += 1

# Calculate % votes
candidatepcntvotes = list(round((x / TotalVotes)*100,0) for x in candidatevotes)

# Output to console
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(TotalVotes))
print('-------------------------')

# Loop thru each candidates
for a in range(0, numberofcandidates):
    print(candidate[a] +  ': ' + str(candidatepcntvotes[a]) + '00%' + ' (' + str(candidatevotes[a]) + ')')
    a += 1

print('-------------------------')
print('Winner: ' + candidate[candidatepcntvotes.index(max(candidatepcntvotes))])
print('-------------------------')

# Output to file
with open(r'C:\Users\sathe\Documents\python-challenge\PyPoll\output.txt', 'w', newline='') as csv_file_out:
    csv_writer = csv.writer(csv_file_out)

    csv_writer.writerow(['Election Results'])
    csv_writer.writerow(['-------------------------'])
    csv_writer.writerow(['Total Votes: ' + str(TotalVotes)])
    csv_writer.writerow(['-------------------------'])

    # Loop thru each candidates
    for a in range(0, numberofcandidates):
        csv_writer.writerow([candidate[a] +  ': ' + str(candidatepcntvotes[a]) + '00%' + ' (' + str(candidatevotes[a]) + ')'])
        a += 1

    csv_writer.writerow(['-------------------------'])
    csv_writer.writerow(['Winner: ' + candidate[candidatepcntvotes.index(max(candidatepcntvotes))]])
    csv_writer.writerow(['-------------------------'])