# Write a program to read through the mbox-short.txt
# and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's
# mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.

file = raw_input("Enter file:")

if len(file) < 1:
    name = "mbox-short.txt"

fh = open(name)

from_lines = []
emails = {}

for line in fh:
    line = line.rstrip()
    if line.find('From ') == 0:
        line = line.split(' ')
        email = line[1]
        if email not in emails:
            emails[email] = 1
        else:
            emails[email] += 1

email = ''
count = 0

for key in emails:
    if emails[key] > count:
        count = emails[key]
        email = key

print "%s %s" % (email, str(count))
