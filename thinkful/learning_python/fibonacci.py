# Provide num and fibonacci will produce a list with that many numbers in the fibonacci sequence

def fibonacci(n):
	if n == 0:
		return [0]
	
	elif n == 1:
		return [0, 1]
	
	else:
		sequence = [0,1]
		while len(sequence) <= n:
			sequence.append(sequence[-2] + sequence[-1])

	return sequence 

def fizbuzz():
	for num in range(1,100):
		if ((num % 3 == 0) and (num % 5 == 0)):
			print "FizBuzz!" 
		elif (num % 3 == 0):
			print "Fizz!"
		elif (num % 5 == 0):
			print "Buzz!"
		else:
			print num





