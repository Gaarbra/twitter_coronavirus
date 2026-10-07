#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# get the numbers for the hashtag we picked
hashtag_counts = counts[args.key]

# make a list of (number, name) pairs
pairs = []
for name in hashtag_counts:
    number = hashtag_counts[name]
    pairs.append((number, name))

# sort the list from the smallest number to the biggest number
pairs.sort()

# keep the last 10 (the biggest ones, still low to high)
top10 = pairs[-10:]

# split the pairs into two lists: names and numbers
labels = []
values = []
for number, name in top10:
    labels.append(name)
    values.append(number)
    print(name, ':', number)

# make the bar graph
plt.figure(figsize=(10,6))
plt.bar(labels, values)
plt.title('Coronavirus (Korean)')
plt.xlabel('language or country')
if args.percent:
    plt.ylabel('fraction of tweets')
else:
    plt.ylabel('number of tweets')
plt.tight_layout()

# save the graph as a png (the # is removed from the name)
filename = os.path.basename(args.input_path) + '_' + args.key.replace('#','') + '.png'
plt.savefig(filename)
print('saved', filename)
