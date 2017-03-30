#Question 1:

import csv
import string

with open('faculty.csv') as csvfile:
    next(csvfile, None)
    readCSV = csv.reader(csvfile, delimiter=',')
    counts = dict()
    for row in readCSV:
        output = row[1]
        if len(output) > 1:
            degree = str(output)
            degree = degree.translate(str.maketrans("", "", string.punctuation))
            words = degree.split()
            for word in words:
                if word not in counts: 
                    counts[word] = 1
                else:
                    counts[word] += 1

print (counts)
print (len(counts))

#Question 2:

import csv
import string
import re

with open('faculty.csv') as csvfile:
    next(csvfile, None)
    readCSV = csv.reader(csvfile, delimiter=',')
    counts = dict()
    for row in readCSV:
        output = row[2]
        if len(output) > 1:
            line = str(output)
            line = line.strip()
            x = re.split("(Professor)+", line)
            del x[-1]
            y = ' '.join(x)
            if y not in counts: 
                counts[y] = 1
            else:
                counts[y] += 1

print (counts)
print (len(counts))

#Question 3:

import csv
import string

with open('faculty.csv') as csvfile:
    next(csvfile, None)
    readCSV = csv.reader(csvfile, delimiter=',')
    emails = list()
    for row in readCSV:
        output = row[3]
        if len(output) > 1:
            x = str(output)
            emails.append(x)

for x in emails:
    print (x)

#Question 4:

import csv
import string
import re

with open('faculty.csv') as csvfile:
    next(csvfile, None)
    readCSV = csv.reader(csvfile, delimiter=',')
    domains = dict()
    for row in readCSV:
        output = row[3]
        if len(output) > 1:
            line = str(output)
            line = line.strip()
            x = re.split("(@)+", line)
            y = x[-1]
            if y not in domains: 
                domains[y] = 1
            else:
                domains[y] += 1

print (domains)
print (len(domains))
