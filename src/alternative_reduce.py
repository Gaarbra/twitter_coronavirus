#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags',nargs='+',required=True)
parser.add_argument('--input_folder',default='outputs')
parser.add_argument('--output_path',default='alternative_reduce.png')
args = parser.parse_args()

# imports
import os
import json
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# make an empty dictionary for each hashtag
# counts['#coronavirus'][75] will be the number of tweets on day 75
counts = {}
for hashtag in args.hashtags:
    counts[hashtag] = {}

# loop over every file in the outputs folder
for filename in sorted(os.listdir(args.input_folder)):

    # only look at the .lang files
    if not filename.endswith('.lang'):
        continue

    # get the date from the filename (example: geoTwitter20-03-15.zip.lang)
    date_text = filename[len('geoTwitter'):len('geoTwitter')+8]
    date = datetime.datetime.strptime(date_text, '%y-%m-%d')
    day_of_year = date.timetuple().tm_yday

    # open the file
    path = os.path.join(args.input_folder, filename)
    with open(path) as f:
        data = json.load(f)

    # add up the tweets for each hashtag on this day
    for hashtag in args.hashtags:
        if hashtag in data:
            total = sum(data[hashtag].values())
        else:
            total = 0
        counts[hashtag][day_of_year] = total

# make the line graph
plt.figure(figsize=(12,6))
for hashtag in args.hashtags:

    # put the days in order, then get the number for each day
    days = sorted(counts[hashtag].keys())
    values = []
    for day in days:
        values.append(counts[hashtag][day])

    plt.plot(days, values, label=hashtag)

plt.title('Hashtag usage during 2020')
plt.xlabel('day of the year')
plt.ylabel('number of tweets')
plt.legend()
plt.tight_layout()

# save the graph as a png
plt.savefig(args.output_path)
print('saved', args.output_path)
