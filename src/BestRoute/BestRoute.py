from collections import defaultdict
from heapq import *
import pandas as pd 
import numpy as np
from vincenty import vincenty
import sys
import os
sys.path.append(os.getcwd())
from testcases.testcases import *

def flattenList(l):
    '''
    This is used to flatten List
    '''
	flat_list = []
	def helper(l):
            # good function
		for i in l:
			if isinstance(i, list):
				helper(i)
			else:
				flat_list.append(i)
	helper(l)
	return flat_list

def covertPathFormat(path):
	'''
	Convert path list into '_' connected path edge pairs
	'''
	out = []
	for i in range(len(path)-1):
		out.append("{0}_{1}".format(path[i],path[i+1]))
	return out

def dijkstra(edges, f, t):
	'''
	Directed dijkstra to find shortest path given a graph
	'''
	g = defaultdict(list)
	for l,r,c in edges:
		g[l].append((c,r))
	q, seen, mins = [(0,f,[])], set(), {f: 0}

	while q:
		(cost,v1,path) = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			path = [ path,v1]
			if v1 == t: 
				return (cost, covertPathFormat(flattenList(path)))
			if g.get(v1,None) == None:
				return float('inf'),''
			for c, v2 in g.get(v1,()):
				if v2 in seen: continue
				prev = mins.get(v2, None)
				next = cost + c

				if prev is None or next < prev:
					mins[v2] = next
					heappush(q, (next, v2, path))
	return float("inf"),''


def findSecondThridShortest(edges,paths,start,end):
	'''
	Remove one path a time and find the corresponding shortest path and store into 
	a dict, pick the top two with shortest path length
	'''
	alt = {}
	for path in paths:
		newEdges = edges.copy()
		newEdges = removeEdge(newEdges,path)

		cost,path = dijkstra(newEdges, start, end)
		if cost not in alt:
			alt[cost] = [path]
		elif alt[cost][0] == path:
			continue
		else:
			alt[cost].append(path)
	# rank all path based on cost value
	alt_rank = []
	for key in sorted(alt):
		alt_rank.extend(alt[key])
	return alt_rank

def printHelper(path,num):
	'''
	Helper function to print output options
	'''
	print("Option {0}:".format(num),end=' ')
	for item in path:
		print(item,end=',')
	print()
	return

def removeEdge(edges,path):
	'''
	remove path from edges
	'''
	b,e = path.split('_')
	for edge in edges:
		start,end,cost = edge
		if b == start and e == end:
			edges.remove(edge)
	return edges

def RouteFinder(edges,start,end):
	'''
	Wrapper function to implement RouteFinder function

	Step 1. Use Dijkstra to find the shortest path
	Step 2. Find the second and third shortest path
	this is achieve by remove one edge from the shortest path a time 
	and then redo the dijkstra algorithm to find the shortest path
	each of the shortest path is stored into a dict and we pick out the two 
	with shortest path length as the the return value 

	'''
	cost1,path1 = dijkstra(edges,start,end)
	alt = findSecondThridShortest(edges,path1,start,end)

	# Print output
	try:
		assert path1 != ''
	except:
		print('Option 1: {0}'.format('NA'))
	else:
		printHelper(path1,1)		
	
	try:
		assert alt[0] != ''
	except:
		print("Option 2: {0}".format('NA'))
	else:
		printHelper(alt[0],2)
	try:
		assert alt[1] != ''
	except:
		print("Option 3: {0}".format('NA'))
	else:
		printHelper(alt[1],3)



def getDistBetweenTwoPoints(L1,L2,df):
	'''
	Calculate distance between two points in locations dataframe 
	using vincenty`s formula. 
	'''
	P1 = df.loc[df['LocationCode']==L1][['Latitude','Longitude']].values
	P2 = df.loc[df['LocationCode']==L2][['Latitude','Longitude']].values
	# print(L1,L2,P1,P2)
	if L1 not in df.LocationCode.values:
		return float('inf')
	if L2 not in df.LocationCode.values:
		return float('inf')
	P1 = np.reshape(P1,(2,1))
	P2 = np.reshape(P2,(2,1))
	distance = vincenty(P1,P2)
	return distance



if __name__ == "__main__":

	trips = pd.read_csv('../data/trips.csv')
	locations = pd.read_csv("../data/locations.csv")

	trips['dist'] = trips[['Origin','Destination']].apply(lambda x: getDistBetweenTwoPoints(x['Origin'],x['Destination'],locations),axis=1)
	edges = trips[['Origin','Destination','dist']].values.tolist()
	
	# Simple Graphy BenchMark	
	print("BenchmarkCase with Simple Graph")
	simpleGraphBenchmark(RouteFinder)

	# Example 1
	start = 'BM'
	end = 'AUSVM'
	print("\nExample 1 \n ----> Route From {0} to {1}:".format(start,end))
	RouteFinder(edges,start,end)
	

	# Example 2
	start = 'BM'
	end = 'NASH'
	print("\nExample 2 \n ----> Route From {0} to {1}:".format(start,end))
	RouteFinder(edges,start,end)
	
	# TestCase 1
	start = 'BM'
	end = 'BOS'
	print("\n TestCase 1 \n ----> Route From {0} to {1}:".format(start,end))
	RouteFinder(edges,start,end)

	# TestCase 2
	start = 'WIND'
	end = 'INDI'
	print("\n TestCase 2 \n ----> Route From {0} to {1}:".format(start,end))
	RouteFinder(edges,start,end)








