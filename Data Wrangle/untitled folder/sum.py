import json
import gzip
import csv

def json_lines_reader(file):
    for line in gzip.open(file):
        yield json.loads(line)

#outcsv = csv.writer(open("issue_summary.csv","w"))
#outcsv.writerow(["issue_or_pr","number","author","open","merge","closed","labels"])
for issue in json_lines_reader("rust_pull_request_comments.json.gz"):
    f = open("demofile2.txt", "a")
    f.write(json.dumps(issue, indent=4))

    #f.close()
    #print json.dumps(issue, indent=4)

    #print json.dumps(issue)






#for issue in json_lines_reader("rust_issues.json.gz"):
    #outcsv.writerow(["issue", issue["number"],
         #issue["user"]["login"],
         #issue["created_at"], 
         #issue.get("merged_at",""),
         #issue.get("closed_at",""),
         #";".join([l["url"].split("/")[-1] for l in issue["labels"]])])
         
#for pr in json_lines_reader("rust_pull_requests.json.gz"):
    #outcsv.writerow(["pr", pr["number"],
         #pr["user"]["login"],
         #pr["created_at"], 
         #pr.get("merged_at",""),
         #pr.get("closed_at",""),
         #";".join([l["url"].split("/")[-1] for l in pr.get("labels",[])])])
         
#print json.dumps(issue, indent=4)
#print json.dumps(pr, indent=4)

#loop through pull request numbers, loop through to_numbers(aka ref. numbers),
#loop through refrence number labels and then...
#if a pull request with no label refrences an issue with a label, 
#then replace the null label with the issue it refrences label.