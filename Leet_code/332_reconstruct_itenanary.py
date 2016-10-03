from collections import defaultdict

class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)

        for journey in tickets:
        	graph[journey[0]].append(journey[1])
        
        # Sort the values in the dictionary graph
        for key, values in graph.items():
        	graph[key] = sorted(graph[key])

        # Given source is JFK, run DFS.
        src = "JFK"
        ans = []
        while(True):
        	ans.append(src)
        	if len(graph[src])== 0:
        		break
        	else:
				temp = graph[src].pop(0)
				src = temp
		return ans

if __name__ == '__main__':
	tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
	s = Solution()
	print s.findItinerary(tickets)