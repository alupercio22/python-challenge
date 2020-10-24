import os
import csv

#set votes to 0
total = 0
khan = 0
correy = 0
li = 0
otooley = 0

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)

    for row in csvreader:
        
        total += 1
        if (row[2] == "Khan"):
            khan += 1
        elif (row[2] == "Correy"):
            correy += 1
        elif (row[2] == "Li"):
            li += 1
        else:
            otooley += 1     
    kahn_percent = "{0:.000%}".format(khan / total)
    correy_percent = "{0:.000%}".format(correy / total)
    li_percent = "{0:.000%}".format(li / total)
    otooley_percent = "{0:.000%}".format(otooley / total)

    winner = max(khan, correy, li, otooley)

    if winner == khan:
        winner_name = "Khan"

    elif winner == correy:
        winner_name = "Correy"

    elif winner == li:
        winner_name = "Li"

    else:
        winner_name = "O'Tooley" 

print("Election Results")
print("---------------------------")
print("Total Votes:", total)
print("---------------------------")
print("Kahn:", kahn_percent, "(",khan,")")
print("Correy:", correy_percent,"(",correy,")")
print("Li:", li_percent,"(",li,")")
print("O'Tooley:", otooley_percent,"(",otooley,")")
print("---------------------------")
print("Winner:", winner_name)
print("---------------------------")

output_path = os.path.join('.', 'PyPoll', 'Resources', 'results.txt')
with open(output_path, 'w') as text_file:
    print("Election Results", file=text_file)
    print("---------------------------", file=text_file)
    print("Total Votes:", total, file=text_file)
    print("---------------------------", file=text_file)
    print("Kahn:", kahn_percent, "(",khan,")", file=text_file)
    print("Correy:", correy_percent,"(",correy,")", file=text_file)
    print("Li:", li_percent,"(",li,")", file=text_file)
    print("O'Tooley:", otooley_percent,"(",otooley,")", file=text_file)
    print("---------------------------", file=text_file)
    print("Winner:", winner_name, file=text_file)
    print("---------------------------", file=text_file)