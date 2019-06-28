import csv
import time
import datetime
import math 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

status = []


new_count = 0 
old_count = 0

outcsv = csv.writer(open("vizPR.csv","w"))
outcsv.writerow(["label","new","old"])

s = pd.date_range('2010', '2019', freq='1Y')  # DatetimeIndex
pd.Series(1, index=s).resample('1Y', how='count')

########################################
countbyyear= dict()
validlabels = [
'A-NLL',
'A-allocators',
'A-amusing',
'A-x86_64',
'A-frontend',
'A-lang',
'A-associated-items',
'A-docs',
'A-debuginfo',
'A-dst',
'A-async-await',
'A-attributes',
'A-build',
'A-bsd',
'A-codegen',
'A-const-fn',
'A-concurrency',
'A-parallel-queries',
'A-closures',
'A-collections',
'A-diagnostics',
'A-destructors',
'A-edition-2018-lints',
'A-iterators',
'A-save-analysis',
'A-io',
'A-lifetimes',
'A-infrastructure',
'A-lint',
'A-linkage',
'A-libs',
'A-llvm',
'A-linux',
'A-bitrig',
'A-dragonflybsd',
'A-macros',
'A-openbsd',
'A-macros-1.2',
'A-mir',
'A-hir',
'A-parser',
'A-plugin',
'A-resolve',
'A-tools',
'A-rust-2018-preview',
'A-rustdoc',
'A-rustbuild',
'A-stability',
'A-traits',
'A-typesystem',
'A-testsuite',
'A-runtime',
'A-syntaxext',
'A-unicode',
'A-windows',
'T-compiler',
'T-core',
'T-dev-tools',
'T-dev-tools-rustdoc',
'T-doc',
'T-infra',
'T-lang',
'T-libs',
'T-release',
'T-rustdoc'
]
validlabels.sort() # to sort the labels
'''
########################################
countbyyear= dict()
for y in s:
	n = str(y)[0:4]
	countbyyear[n] = dict()
	for l in validlabels:
		countbyyear[n][l] = 0
		countbyyear[n]['Unlabeled'] = 0
########################################
countbyyear= dict()
'''
for row in csv.DictReader(open("/Users/valazeinali/Desktop/New Stuff CMU/newbie_activity.csv")):

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
	#print(labels)

	#print(actor,time,labels,first_action,team,effort,prs,status)
	#print(status)
	#if status != "old": # not really important
		#new_count = new_count + 1
	#else:
		#old_count = old_count + 1

	if time == "2010":

		rowlabels = set()
		## create a dict for new and for old
		## create a data structire that hold 
		## Below is desired table
		#          | Label | New | Old.|
		#          |-------------------|
		#          | A-xyz  |  3 | 1   |
		#          | A-BCA  |  5 | 1   |
		#          | T-JKL  |  5 | 3   |
		for label in labels:
			if label in validlabels:
				rowlabels.add(label)
			if len(rowlabels) == 1:
				label = rowlabels[0]
			elif len(rowlabels) == 0:
				label = 'Unlabeled'
				#print(label)
			else:
				label = 'Unlabeled'
			print(label,status)
		#for i in status:
			#if i in status == "new":
				#new_count = new_count + 1
				#print(new_count)
			#elif i in status != "new":
				#old_count = old_count + 1
			#else:
				#new_count = 0
				#old_count = 0

		#outcsvv = csv.writer(open("2010.csv","w"))
		#outcsvv.writerow([label,status,new_count/3,"old::",old_count])
'''
			for labellist in label:
				for statuslist in status:
				

				
			#print(countbyyear[label][oldstatus][newstatus])

	##print(actor,time,labels,first_action,team,effort,prs,status)

	#outcsv.writerow([actor,time,labels,first_action,team,effort,status])

	#print(actor,time,labels,first_action,team,effort,prs,status)
	#print("# new: ",new_count,"# Old: ",old_count)
	#print((new_count/old_count)*100)
	
	for y in s: 
		n = str(y)[0:4]
		countbyyear[n] = dict()
		for l in validlabels:
			countbyyear[n][l] = 0
		countbyyear[n]['Unlabeled'] = 0

		rowlabels = set()

		for label in labels:
			if label in validlabels:
				rowlabels.add(label)
		if len(rowlabels) == 1:
			for l in rowlabels:
				label = l
		elif len(rowlabels) == 0:
			label = 'Unlabeled'
		else:
			label = l


		#countbymonth[str(row[2])[0:4][label][status] += int[effort]
	years = countbyyear.keys()
	#months.sort()
	sorted(years)

	outcsv = csv.writer(open("vizPR111.csv","w"))
	outcsv.writerow(years)
	'''
