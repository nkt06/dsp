#QUESTION 6

import csv
import string
import re

with open('faculty.csv') as csvfile:
    next(csvfile, None)
    readCSV = csv.reader(csvfile, delimiter=',')
    counts = dict()
    for row in readCSV:
        output = row[0]
        degree = row[1]
        degree = degree.strip()
        title = row[2]
        line = title.strip()
        line = str(line)
        x = re.split("(Professor)+", line)
        x = list(filter(None, x))
        del x[-1]
        y = ' '.join(x)
        email = row[3]
        words = output.split()
        last_name = words[-1]
        desc = list()
        desc.append(degree)
        desc.append(y)
        desc.append(email)
        if last_name not in counts: 
            counts[last_name] = list()
            counts[last_name].append(desc)
        else:
            counts[last_name].append(desc)
                    
print (counts)

#QUESTION 7

import csv
import string
import re

with open('faculty.csv') as csvfile:
    next(csvfile, None)
    readCSV = csv.reader(csvfile, delimiter=',')
    counts = dict()
    for row in readCSV:
        output = row[0]
        words = output.split()
        first_name = words[0]
        last_name = words[-1]
        name = (first_name, last_name)
        degree = row[1]
        degree = degree.strip()
        title = row[2]
        line = title.strip()
        line = str(line)
        x = re.split("(Professor)+", line)
        x = list(filter(None, x))
        del x[-1]
        y = ' '.join(x)
        email = row[3]
        words = output.split()
        last_name = words[-1]
        desc = list()
        desc.append(degree)
        desc.append(y)
        desc.append(email)
        counts[name] = list()
        counts[name].append(desc)

#QUESTION 8 (continued from QUESTION 7)
import collections
t = collections.OrderedDict(sorted(counts.items(), key=lambda xy: xy[0][1]))

print (t)
