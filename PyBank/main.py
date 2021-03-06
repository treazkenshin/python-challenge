#import libraries
import os
import csv
​
#input file (CSV format)
csvPath = os.path.join("/Users/treazkenshin/Downloads/cwru-cle-data-pt-01-2021-u-c-master-Homework-03-Python/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
output file (Text format)
txtPath = os.path.join("/Users/treazkenshin/Downloads/cwru-cle-data-pt-01-2021-u-c-master-Homework-03-Python/Homework/03-Python/Instructions/PyBank/Resources/budget_data.txt")
​
#create variables
minBudget = 0
maxBudget = 0
minMonth = ''
maxMonth = ''
​
minBudgetDelta = 0
maxBudgetDelta = 0
minMonthDelta = ''
maxMonthDelta = ''
​
sumDelta = 0
totalBudget = 0
lastBudget = 0
count = 0
​
#read csv
​
with open(csvPath) as csvfile:
​
    # CSV reader
    csvBudgetData = csv.DictReader(csvfile, delimiter=',')
​
    for monthData in csvBudgetData:
        # count the rows
        count = count + 1
        
        # Extract the data of interest
        thisMonth  = monthData['Date']
        thisBudget = int(monthData['Profit/Losses'])
​
        totalBudget = totalBudget + thisBudget
​
        # Is this a new minimum, yes save it
        if thisBudget < minBudget:
            minBudget = thisBudget
            minMonth = thisMonth
​
        # Is this a new maximum, yes save it
        if thisBudget > maxBudget:
            maxBudget = thisBudget
            maxMonth = thisMonth
​
        # If we are past the first row, do changes between rows
        if count > 1:
            delta = thisBudget - lastBudget
            sumDelta = sumDelta + delta
​
            if delta < minBudgetDelta:
                minBudgetDelta = delta
                minMonthDelta = thisMonth
            if delta > maxBudgetDelta:
                maxBudgetDelta = delta
                maxMonthDelta = thisMonth
                
        # save the current data for calculating next delta
                lastBudget = thisBudget
        
 ​
​
outText = '''
Financial Analysis
----------------------------
Months:         %d
Total:          $%d
Minimum:        %s $%d
Maximum:        %s $%d
Minimum Change: %s $%d
Maximum Change: %s $%d
Average Change: $%.2f
'''% (
count,
totalBudget,
minMonth,minBudget,
maxMonth,maxBudget,
minMonthDelta,minBudgetDelta,
maxMonthDelta,maxBudgetDelta,
float(sumDelta)/float(count-1)
)
​
print(outText)
​
with open(txtPath,"w") as txtFile:
    txtFile.write(outText)
