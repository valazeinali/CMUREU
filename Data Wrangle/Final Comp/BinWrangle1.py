import csv
import pandas as pd

array = []

outcsv = csv.writer(open("wrangled4.csv","w"))
outcsv.writerow(["open","additions","labels"])
s = pd.date_range('2014-02', '2019-07', freq='1M')  # DatetimeIndex
pd.Series(1, index=s).resample('M', how='count')

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

countbymonth = dict()
for m in s:
	n = str(m)[0:7]
	countbymonth[n] = dict()
	for l in validlabels:
		countbymonth[n][l] = 0
	countbymonth[n]['Unlabeled'] = 0
	countbymonth[n]['Multi'] = 0

with open('thisisit.csv','rt')as f:
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
outcsv = csv.writer(open("wrangled4.csv","w"))
outcsv.writerow(['label'] + months)
for label in validlabels + ['Unlabeled', 'Multi']:
	row = [label]
	for month in months:
		row.append(countbymonth[month][label])
	outcsv.writerow(row)

