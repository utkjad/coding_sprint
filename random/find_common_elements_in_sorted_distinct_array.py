
def find_common_elements(l1=[],l2=[]): 
	# If one of the list is empty, return None
	if not l1 or not l2:
		return None
	else:
		i = 0
		j = 0
		while True:
			if l1[i] == l2[j]:
				print l1[i]
				i += 1
				j += 1
			elif l1[i] > l2[j]:
				j += 1
			elif l1[i] < l2[j]:
				i += 1
			# Exit condition - if you reach at the end of any list
			# there is no point in advancing ahead.
			if i == len(l1) or j == len(l2):
				break

if __name__ == '__main__':
	find_common_elements([3,6,7,14,25],[3,5,7,14,19,23,25])
	find_common_elements([],[2,3,4,5,5])
	find_common_elements([3,5,7,14,19,23,25], [3,6,7,14,15])

			


