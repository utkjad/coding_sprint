from collections import defaultdict



	def calcEquation(equations, values, queries):
		"""
		:type equations: List[List[str]]
		:type values: List[float]
		:type queries: List[List[str]]
		:rtype: List[float]
		"""
		nodes = set()
		for i in equations:
			nodes.update(i)
		
		edges = defaultdict(list)

		for i, (x, y) in enumerate(equations):
			edges[x].append((y, values[i]))
			if values[i] != 0:
				edges[y].append((x, 1.0 / values[i]))
		
		visited = {}
		for i in nodes:
			visited[i] = False

		ans = []
		for x, y in queries:
			# Isolated node
			if x not in edges or y not in edges:
				ans.append(-1.0)
			# Same element
			elif x == y:
				ans.append(1.0)
			# Else do the DFS multiplication
			else:
				t = dfs(1, x, y, edges, visited)
				ans.append(t if t else -1.0)
		return ans


	def dfs(val, _from, to, edges, visited):
		for node,weight in edges[_from]:
			# If already visited, conitnue
			if visited[node]:
				continue
			# Now that we have reached our destination, return the value
			if node == to:
				return val*weight

			# Mark current as visited
			visited[node] = True
			# Continue the dfs...
			t = dfs(val*weight, node, to, edges, visited)
			# Mark node as unvisited as the need for the node is over
			visited[node] = False

			# Return
			if t:
				return t
		return None

if __name__ == '__main__':
	equations = [ ["a", "b"], ["b", "c"] ]
	values = [2.0, 3.0]
	queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
	print calcEquation(equations, values, queries)