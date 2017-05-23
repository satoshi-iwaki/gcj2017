import math

class Pancake:
	def __init__(self, index, r, h):
		self.index = index
		self.r = r
		self.h = h

		self.top_area = r ** 2
		self.side_area = r * 2 * h
		self.total_area = self.top_area + self.side_area
	
	def __hash__(self):
		return hash(self.index)
	
	def __eq__(self, other):
		return self.index == other.index
	
	def __repr__(self):
		return '{index:%s, r: %s, h: %s, side: %s, top: %s}' % (self.index, self.r, self.h, self.side_area, self.top_area)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  pancakes = []
  for j in xrange(1, n + 1):
  	r, h = [int(s) for s in raw_input().split(" ")]
  	pancake = Pancake(j, r, h)
  	pancakes.append(pancake)

  sorted_pancakes_by_top_area = sorted(pancakes, key=lambda x: x.top_area, reverse=True)[:k]
  sorted_pancakes_by_side_area = sorted(pancakes, key=lambda x: x.side_area, reverse=True)[:k]

  sorted_pancakes = []
  sorted_pancakes = sorted_pancakes + sorted_pancakes_by_top_area
  sorted_pancakes = sorted_pancakes + sorted_pancakes_by_side_area
  sorted_pancakes = list(set(sorted_pancakes))
  sorted_pancakes = sorted(sorted_pancakes, key=lambda x: x.total_area, reverse=True)[:k]
  sorted_pancakes = sorted(sorted_pancakes, key=lambda x: x.r, reverse=True)
  # print "Sorted pancakes = {}".format(sorted_pancakes)

  area = 0
  for pancake in sorted_pancakes:
  	area = area + pancake.side_area

  area = area + sorted_pancakes[0].top_area

  print "Case #{}: {:.9f}".format(i, area * math.pi)

  # check out .format's specification for more formatting options
