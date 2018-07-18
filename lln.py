#Law of large numbers
import random
def prob(n):
	results = [random.choice([0,1]) for i in range(n)]
	return float(sum(results))/n
for i in range(1,1000,10):
		print prob(i)
