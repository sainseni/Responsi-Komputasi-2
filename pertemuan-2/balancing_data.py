

def compensate_imbalance(data):	
	""" this function will return list that contains weights each class 
	data: vector or array 1-D
	"""
	unix_count = {} # dictionary that contains class with its frequency
	weights = [] # list that containes weights each class

	for item in data:
		if item not in unix_count:
			unix_count[item] = 0

		if item in unix_count:
			unix_count[item] += 1

	for item in unix_count:
		weights.append(unix_count[item]/len(data))

	return weights


example_data = [1, 1, 1, 2, 2]

# call compensate_imbalance function and print it
print(compensate_imbalance(example_data))



