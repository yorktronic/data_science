############################
#
# Exercsie in Markov Models - the model is the stock market which can have one of three 
# states: Bull, Bear, or Stagnant. The decimals are the probabilities of transition between
# each of the states
#
############################

import pandas as pd
pd.set_option('precision', 5)

df = pd.DataFrame({'bull': [0.9, 0.15, 0.25], 'bear': [0.075, 0.8, 0.25], 'stag': [0.025, 0.05, 0.5]}, index=['bull', 'bear', 'stag'])

n = 5

print "Original transitional probabilities: \n"
print df
print "\n"

def state(n):
	i = 1
	global df
	while i < n:
		df = df.dot(df)
		i += 1
	print "Tranisitional probabilities after {} transitions: \n".format(n)
	print df

state(n)
