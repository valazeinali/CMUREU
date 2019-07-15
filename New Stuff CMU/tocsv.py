import csv
import time
import datetime
import math 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

status = []
effort = []

outcsvv = csv.writer(open("reldata.csv","w"))
outcsvv.writerow(['actor','time','labels','actors_first_action','effort','prs','status'])

for row in csv.DictReader(open("newbie_activity.csv")):


	actor = row["actor"]
	temp = row["time"] # only getting the year from when author makes a commit
	time = temp[0:4] # only getting the year of the time when an author makes a commit
	labels = row["tags"].split(",") # getting all labels of the commit
	temp1 = row["actors_first_action"] # only getting the year from when author made their first action
	first_action = temp1[0:4] # only getting the year of the time when an author made their first action
	team = row["actors_team"].split(',') # the team(s) the author is on
	effort = (int(row["insertions"]) + int(row["deletions"])) # total amount of effort put into the commit 
	prs = row["prs"].split(",") # getting pull request number(s)


	if time != first_action: # comparing the commit time and authors first action
		status = "old" # they are classified "old" if they have commited in a year that is not the year they made thier "first_action"
	else:
		status = "new" # they are classified "new" if they have commited in a year that is not the year they made thier "first_action"
	

	outcsvv.writerow([actor,temp,labels,temp1,effort,prs,status])
