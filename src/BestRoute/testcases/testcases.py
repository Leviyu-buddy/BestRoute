

def simpleGraphBenchmark(RouteFinder):
	'''
	Test case with a simple graph
	'''
	edges = [
	["A", "B", 7],
	("A", "D", 5),
	("B", "C", 1),
	("D", "B", 2),
	("B", "E", 7),
	("C", "E", 5),
	("D", "E", 15),
	("D", "F", 6),
	("E", "F", 8),
	("G", "E", 9),
	("F", "G", 11.2),
	("C", "G", 1)
	]
	start = 'A'
	end = 'G'
	print("--> Edges are", edges)
	print("--> Start from {0} end to {1}".format(start,end))
	RouteFinder(edges,start,end)
	return

