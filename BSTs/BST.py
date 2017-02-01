class Node(object):
	"""node of the tree"""
	def __init__(self, key):
		self.left = None
		self.value = key
		self.right = None

class BST(object):
	"""BST"""
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			self.__insert(self.root, value)

	def __insert(self, node, someValue):
		if node.value > someValue:
			if node.left is None:
				node.left = Node(someValue)
			else:
				self.__insert(node.left, someValue)
		else:
			if node.right is None:
				node.right = Node(someValue)
			else:
				self.__insert(node.right, someValue)

	def inorder(self, root):
		if root:
			self.inorder(root.left)
			print root.value
			self.inorder(root.right)
		return

# driver program

b = BST()
b.insert(50)
b.inorder(b.root)
b.insert(30)
b.insert(30)
b.insert(70)
b.insert(20)
b.insert(40)
b.insert(60)
b.insert(80)
b.insert(15)
b.insert(25)
b.insert(35)
b.insert(45)
b.insert(33)
b.insert(37)
print "print now"
b.inorder(b.root)


	# def __getmin(self, node):
	# 	if node.left:
	# 		self.__getmin(node.left)
	# 	else:
	# 		return node

	# def delete(self, value):
	# 	# Find the node first of all
	# 	# if it has no children just delete the reference.
	# 	# if it has only left node, replace with left node.
	# 	# if it has only right node, replace with right node.
	# 	# if it has both children find minimum in the right subtree

	# 	if self.root is None:
	# 		return -1
	# 	else:
	# 		if 



