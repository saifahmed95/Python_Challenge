import os
import csv
import operator


#Initialize Variables
vote_count=0
dashes="-------------------------"
candidates = []
vote_count_candidate = {}

election_csv = os.path.join("c:/", "Users", "mango", "Desktop", "Python_Challenge","PyPoll","election_data.csv")


with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        vote_count = vote_count + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_count_candidate[row[2]] = 1
        else:
            vote_count_candidate[row[2]] = vote_count_candidate[row[2]] + 1



winner = max(vote_count_candidate.items(), key=operator.itemgetter(1))[0]

print(f"Election Results") 
print(f"{dashes}")
print(f"Total Votes: {vote_count}")
print(f"{dashes}")
for c, v in vote_count_candidate.items():
    print(c, "{:.3f}".format(round(((v/vote_count)*100),3)) + "%","(",(str(v)),")")
print(f"{dashes}")   
print(f"Winner: " + str(winner) +'\n')
print(f"{dashes}")



output_file = open("PyPoll.txt","w") 
 
output_file.write("Election Results"+ '\n') 
output_file.write(f"{dashes}" + '\n')
output_file.write(f"Total Votes: {vote_count}"+ '\n')
output_file.write(f"{dashes}" + '\n')
for c, v in vote_count_candidate.items():   
    output_file.write(c+" "+"{:.3f}".format(round(((v/vote_count)*100),3)) + "%"+"  ("+(str(v))+")"+ '\n')
output_file.write(f"{dashes}" + '\n')   
output_file.write(f"Winner: " + str(winner) + '\n')
output_file.write(f"{dashes}" + '\n')
output_file.close() 