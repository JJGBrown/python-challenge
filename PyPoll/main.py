import csv

total_votes = 0
candidates = {'Khan': 0, 'Correy': 0, 'Li': 0, "OTooley": 0}
winner = ''
votes = 0

print(candidates)

with open('PyPoll/Homework_03-Python_PyPoll_Resources_election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            # Row[0] = Voter ID, Row[2] = Candidate
            line_count += 1
        else:
            # Getting error when accessing dictionary using this O'Tooley as key
            if row[2] == "O'Tooley":
                candidates["OTooley"] += 1
            else:
                candidates[row[2]] += 1
            line_count += 1
    
    total_votes = line_count - 1
    for key in candidates:
        if votes < candidates[key]:
            votes = candidates[key]
            winner = key
    print('Election Results')
    print('----------------------------')
    print(f'Total Votes: {total_votes}')
    print('----------------------------')
    print(f'Khan: {round((candidates["Khan"] / total_votes) * 100, 3)}% ({candidates["Khan"]})')
    print(f'Correy: {round((candidates["Correy"] / total_votes) * 100, 3)}% ({candidates["Correy"]})')
    print(f'Li: {round((candidates["Li"] / total_votes) * 100, 3)}% ({candidates["Li"]})')
    print(f'O\'Tooley: {round((candidates["OTooley"] / total_votes) * 100, 3)}% ({candidates["OTooley"]})')
    print('----------------------------')
    print(f'Winner: {winner}')
    print('----------------------------')
    
    Result = open("PyPoll/Result.txt","a")
    Result.write('Election Results\n')
    Result.write('----------------------------\n')
    Result.write(f'Total Votes: {total_votes}\n')
    Result.write('----------------------------\n')
    Result.write(f'Khan: {round((candidates["Khan"] / total_votes) * 100, 3)}% ({candidates["Khan"]})\n')
    Result.write(f'Correy: {round((candidates["Correy"] / total_votes) * 100, 3)}% ({candidates["Correy"]})\n')
    Result.write(f'Li: {round((candidates["Li"] / total_votes) * 100, 3)}% ({candidates["Li"]})\n')
    Result.write(f'O\'Tooley: {round((candidates["OTooley"] / total_votes) * 100, 3)}% ({candidates["OTooley"]})\n')
    Result.write('----------------------------\n')
    Result.write(f'Winner: {winner}\n')
    Result.write('----------------------------\n')
    Result.close()
    