def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    min_r = 0
    min_c = 0

    max_r = len(matrix) - 1
    max_c = len(matrix[0]) - 1

    result_list = []

    while min_r <= max_r:
    	if min_r == max_r:
    		result_list.append(matrix[min_r][min_c])
    		break
    	for i in range(min_r ,max_c + 1):
    		result_list.append(matrix[min_r][i])

    	for i in range(min_r + 1, max_r + 1):
    		result_list.append(matrix[i][max_c])

    	for i in range(max_c - 1, min_c-1, -1):
    		result_list.append(matrix[max_r][i])

    	for i in range(max_r - 1, min_r, -1):
    		result_list.append(matrix[i][min_c])

    	# At the end do increment/decrement min and max
    	min_r += 1
    	min_c += 1

    	max_r -= 1
    	max_c -= 1

    return result_list

print spiralOrder([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
# spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])

