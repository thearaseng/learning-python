#!/usr/bin/env python3

ages = {'kevin': 59, 'bob': 40}

print(ages['kevin'])

# update key value
ages['kevin'] = 60

# add new key-value
ages['john'] = 30

print(ages)

# delete key
del ages['john']

print(ages)

# get keys
print(ages.keys())