import collections

testlist = [1,4,5,6,9,9,9]

c = collections.Counter(testlist)

print c

# Calculate the number of instances in the list
count_sum = sum(c.values())

for k, v in c.iteritems():
	print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)