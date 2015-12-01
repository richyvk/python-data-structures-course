# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day
# for each of the messages. You can pull the hour out
# from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

hours = {}

for line in handle:
    line = line.strip()
    if line.find('From ') == 0:
        hour_sent = line[line.find(':')-2:line.find(':')]
        # use dict get method to retrieve each hour_sent, or add it
        # to the dict if it isn't present already (with default value of 0).
        # Then set the value to value + 1
        hours[hour_sent] = hours.get(hour_sent, 0) + 1

tups = hours.items()  # get keys/values from hours as list of tuples
tups.sort()  # sort by keys (first item in each tuple)

for tup in tups:
    print tup[0], str(tup[1])
