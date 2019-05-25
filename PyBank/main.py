import csv

# declare variables and list
monthcnt = 0
total = 0
current = []
previous = []
change = []
Average = 0
cntforavg = 0
monthsandyears = []

# open, read the csv file and loop through
with open(r'C:\Users\sathe\Documents\python-challenge\PyBank\budget_data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    # skip header
    next(csv_reader)

    for row in csv_reader:
        # Insert all data into list except first one.
        if monthcnt != 0 and total != 0:
            current.append(row[1])
            monthsandyears.append(row[0])
        # Insert all data into list; can delete last one later
        previous.append(row[1])
        monthcnt = monthcnt + 1
        total = total + int(row[1])

# delete last 
del previous[-1]

# Calculate Change (Current month - previous month) and average
for index, i in enumerate(current):
    change.append((int(i) - int(previous[index])))

for each in change:
    Average = Average + each
    cntforavg = cntforavg + 1

Average = round(Average / cntforavg, 2)

# Print output to console
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(monthcnt))
print('Total: $' + str(total))
print('Average Change: $' + str(Average))
print('Greatest Increase in Profits: ' + monthsandyears[change.index(max(change))] + ' ($' + str(max(change)) + ')')
print('Greatest Decrease in Profits: ' + monthsandyears[change.index(min(change))] + ' ($' + str(min(change)) + ')')

# Write output to a file
with open(r'C:\Users\sathe\Documents\python-challenge\PyBank\budget_data_output.csv', 'w', newline='') as csv_outputfile:
    csv_writer = csv.writer(csv_outputfile)

    csv_writer.writerow(['Financial Analysis'])
    csv_writer.writerow(['----------------------------'])
    csv_writer.writerow(['Total Months: ' + str(monthcnt)])
    csv_writer.writerow(['Total: $' + str(total)])
    csv_writer.writerow(['Average Change: $' + str(Average)])
    csv_writer.writerow(['Greatest Increase in Profits: ' + monthsandyears[change.index(max(change))] + ' ($' + str(max(change)) + ')'])
    csv_writer.writerow(['Greatest Decrease in Profits: ' + monthsandyears[change.index(min(change))] + ' ($' + str(min(change)) + ')'])