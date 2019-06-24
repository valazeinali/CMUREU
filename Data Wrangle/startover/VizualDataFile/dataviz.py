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
