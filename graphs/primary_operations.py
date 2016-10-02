# Just to revise the way graphs work, RIGHT from scratch.
# this is implementation using Adjacency lists
class Vertex:
	def __init__(self, value):
		self._value = value
		self.adjacent = {}

	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self,value):
		self._value	= value

	def add_neighbour_vertex(self, neighbour, weight = 0):
		self.adjacent[neighbour]= weight

	def get_connected_vertices(self):
		return self.adjacent.keys()

	def get_edge_weight(self, neighbour):
		return self.adjacent[neighbour]

	def __str__(self):
		return str(self._value) + ' in str Adjacent Nodes - ' + str([x for x in self.adjacent])

	def __repr__(self):
		return str(self._value) + '  in repr Adjacent Nodes - ' + str([x for x in self.adjacent])


c = Vertex(10)
d = Vertex(50)
c.add_neighbour(d.value, 10)
print str(c)
print str(d)
print(repr(c))
print c.adjacent
