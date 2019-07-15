import csv
import time
import datetime
import math 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

old_status = []
new_status = []

########################################
countbyyear= dict()
validlabels = [
'A-NLL',
'A-allocators',
'A-amusing',
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
'T-rustdoc',
'E-easy'
]
validlabels.sort() # to sort the labels

counts = dict()
for label in validlabels:
	counts[label] = {'new': 0, 'old': 0}
counts['Unlabeled'] = {'new': 0, 'old': 0}

outcsvv = csv.writer(open("2009.csv","w"))
outcsvv.writerow(['label','new','old'])

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
	

	if time == "2017": # change this to the year you want eg., 2010,2011,2012,2013

		validrowlabels = set()		

		nolabels = True
		for label in labels:
			if label in validlabels:
				nolabels = False
				counts[label][status] += 1

		if nolabels:
			counts['Unlabeled'][status] += 1

outcsvv.writerow(['Unlabeled',counts['Unlabeled']['new'],counts['Unlabeled']['old']])
for label in validlabels:
	outcsvv.writerow([label,counts[label]['new'],counts[label]['old']])
