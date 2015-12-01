# Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as

captured = []

with open('mbox-short.txt') as f:
    text = f.read().splitlines()

# find lines in text starting with X-DSPAM-Confidence,
# extract number from end of each matching line and convert to float
for line in text:
    if line.startswith("X-DSPAM-Confidence"):
        captured.append(float(line[line.find(':')+1:].strip()))

# print sum of captured list elements / length of list (e.g. average)
print "Average spam confidence: %d" % (sum(captured) / len(captured))
