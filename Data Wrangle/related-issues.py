#from pymongo import MongoClient, ASCENDING, DESCENDING
#from configur import * 
import json
import pdb
#import git_comment_conventions as gcc
import csv

#db = MongoClient("mongodb://%s:%s@127.0.0.1:27017/ghtorrent?authSource=ghtorrent" % (username, password))["ghtorrent"]
 
refs = csv.writer(open("/tmp/rust-refs.csv","w"))
refs.writerow(["rec_type","rec_label","number","created_at","to_owner","to_repo","to_number"])
#tags = csv.writer(open("/tmp/rust-labels.csv","w"))
#tags.writerow(["action","owner","repo","number","tagger","created_at","tag"])
def dorow(rec_type, row, number=None):
    features = {}
    if row["body"] is None: return
    gcc.find_issue_references(features, row["body"])
    if len(features["issues"]) > 0:
        for i in features["issues"]:
            refs.writerow([rectype, row["owner"], row["repo"], number, row["user"]["login"], row["created_at"],
                  i["parts"][0].replace("%OWNER%",row["owner"]), i["parts"][1].replace("%PROJECT%",row["repo"]), i["parts"][2]])

def checkall(owner, repo):
        print "Labels"
        for row in db.issue_events.find({"owner":owner, "repo": repo, "label": {"$exists": True}}):
            try:
              actor = row["actor"]["login"]
            except Exception, e:
              actor = "unknown"
            tags.writerow([row["event"], owner, repo, row["issue_id"], actor, row["created_at"], row["label"]["name"].encode("utf-8")])
        print "prs"
        for row in db.pull_requests.find({"owner":owner, "repo": repo}):
            dorow("pull_request", row, number=row["number"])
        print "issues"
        for row in db.issues.find({"owner":owner, "repo": repo}):
            dorow("issue", row, number=row["number"])
        print "issue-comments"
        for row in db.issue_comments.find({"owner":owner, "repo": repo}):
            dorow("issue-comment", row, number=row["issue_id"])
        print  "pr-comments"
        for row in db.pull_request_comments.find({"owner":owner, "repo": repo}):
            dorow("pull-request-comment", row, number=row["pullreq_id"])

checkall("rust-lang","rust")
checkall("rust-lang","rfcs")

