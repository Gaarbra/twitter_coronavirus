#!/usr/bin/env python3
import argparse
import json
from collections import Counter, defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

total = defaultdict(lambda: Counter())

for path in args.input_paths:
    with open(path) as f:
        daily = json.load(f)
        for hashtag in daily:
            total[hashtag].update(daily[hashtag])

with open(args.output_path, 'w') as f:
    json.dump(total, f)
