import csv 

status = []

easy_count = 1

validlabels = ["E-easy"]

outcsv = csv.writer(open("MLdataset.csv","w"))
outcsv.writerow(['User','additions','deletions','num_easy_y1','year','status'])

for row in csv.DictReader(open("/Users/valazeinali/Desktop/New Stuff CMU/newbie_activity.csv")):

	actor = row["actor"]
	temp = row["time"] # only getting the year from when author makes a commit
	time = temp[0:4] # only getting the year of the time when an author makes a commit
	labels = row["tags"].split(",") # getting all labels of the commit
	temp1 = row["actors_first_action"] # only getting the year from when author made their first action
	first_action = temp1[0:4] # only getting the year of the time when an author made their first action
	additions = row["insertions"]
	deletions = row["deletions"]
	effort = (int(row["insertions"]) + int(row["deletions"])) # total amount of effort put into the commit

	

		#for i in actor:
	if time == first_action: # comparing the commit time and authors first action
		status = "new" # they are classified "old" if they have commited in a year that is not the year they made thier "first_action"
	elif int(time) == int(first_action) +1: 
		status = "new"
	elif int(time) == int(first_action) +2: 
		status = "new"
	elif int(time) == int(first_action) +3: 
		status = "intermediate"
	elif int(time) == int(first_action) +4: 
		status = "intermediate"
	elif int(time) == int(first_action) +5: 
		status = "intermediate"	
	else:
		status = "advanced" # they are classified "advanced" if they have commited in a year that is in 2016+

	if "E-easy" in labels:
		easy_count = 1 # where there is a E-easy label present we add 1 to the list 
	else:
		easy_count = 0 # we dont add a count to the list if ! present 
		

	outcsv.writerow([actor,additions,deletions,easy_count,time,status])

