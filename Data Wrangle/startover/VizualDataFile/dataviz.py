'''
import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('vizPR1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[1]))
        y.append(str(row[0]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title(row[1])
plt.legend()
plt.show()
#3999999999
'''

import csv
import pandas as pd
import matplotlib.pyplot as plt

#s = line[1].value_counts() ## Counts the occurrence of unqiue elements and stores in a variable called "s" which is series type
#$new = pd.DataFrame({'FuncGroup':s.index, 'Count':s.values})  ## Converting series type to pandas df as plotly accepts dataframe as input. The two columns of df is FuncGroup which is being made by index of series and new variable called count which is made by values of series s.
#path = 'c:\\temp\\'
x = []
y = []

file=open( "vizPR1.CSV", "r")
reader = csv.reader(file)
data_list = list(csv.reader('vizPR1.CSV'))
for i in data_list:
	print(i)

    #s = i[1].value_counts()
new = pd.DataFrame({'FuncGroup':s.index, 'Count':s.values}) 

for line in reader:

    t=line[0],line[1]

    x.append(line[0])
    y.append(line[1])

    print(t)

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('month')
plt.ylabel('frequency')
plt.title("A-NLL")
plt.legend()
plt.show()