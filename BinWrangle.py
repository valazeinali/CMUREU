import csv
import pandas as pd
array = []
outcsv = csv.writer(open("wrangled.csv","w"))
outcsv.writerow(["open","additions","labels"])
s = pd.date_range('2014-02', '2019-07', freq='1M')  # DatetimeIndex
pd.Series(1, index=s).resample('M', how='count')

validlabels = [
'A-NLL',
'A-allocators',
'A-async-await',
'A-attributes',
'A-build',
'A-codegen',
'A-const-fn',
'A-diagnostics',
'A-edition-2018-lints',
'A-iterators',
'A-lifetimes',
'A-lint',
'A-macros',
'A-macros-1.2',
'A-mir',
'A-rust-2018-preview',
'A-rustbuild',
'A-stability',
'A-traits',
'A-unicode',
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

countbymonth = dict()
for m in s:
	n = str(m)[0:7]
	countbymonth[n] = dict()
	for l in validlabels:
		countbymonth[n][l] = 0
	countbymonth[n]['Unlabeled'] = 0
	countbymonth[n]['Multi'] = 0

with open('data4newSummarize.csv','rt')as f:
  data = csv.reader(f)
  for row in data: 
       array = row
       rowlabels = set()
       if row[1] == 'additions':
       		continue
       for label in row[2].split(';'):
       		if label in validlabels:
       			rowlabels.add(label)
       label = 'aAAAA'
       if len(rowlabels) == 1:
       		for l in rowlabels:
       			label = l
       elif len(rowlabels) == 0:
       		label = 'Unlabeled'
       else:
       		label = 'Multi'
       print(row)
       countbymonth[str(row[0])[0:7]][label] += int(row[1])

months = countbymonth.keys()
months.sort()
outcsv = csv.writer(open("wrangled2.csv","w"))
outcsv.writerow(['label'] + months)
for label in validlabels + ['Unlabeled', 'Multi']:
	row = [label]
	for month in months:
		row.append(countbymonth[month][label])
	outcsv.writerow(row)

