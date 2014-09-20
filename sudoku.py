import numpy as np

class Node:
	def __init__(self, x, y, value, level):
		self.x = x
		self.y = y
		self.value = value
		self.level = level

	def children(self):
		if self.y == 8:
			x = self.x + 1
			y = 0
		else:
			x = self.x
			y = self.y + 1
		nodes = []
		values = possible_values(board, x, y)
		values.reverse()
		for i in values:
			nodes.append(Node(x, y, i, self.level + 1))
		return nodes

board = np.array([[0 for x in range(9)] for x in range(9)])

positions = [(4,4)]
board[4][4] = 7

start = Node(0, -1, 0, 0)
stack = [start]

def solve(board):
	current = start
	while current.level != 81:
		stack.extend(current.children())
		if current.children() == []:
			board[current.x][current.y] = 0
		if len(stack) != 0:
			current = stack.pop()
		else:
			return "Unsolvable sudoku puzzle!"
		board[current.x][current.y] = current.value
	return board

def possible_values(board, x, y):
	if (x,y) in positions:
		return [board[x][y]]
	values = [n + 1 for n in range(9)]
	row_ = [i for i in values if i not in row(board, x)]
	column_ = [j for j in values if j not in column(board, y)]
	box_ = [k for k in values if k not in box(board, x, y)]
	return list(set(row_) & set(column_) & set(box_))

def row(board, x):
	return filter(lambda i: i != 0, board[x])

def column(board, y):
	return filter(lambda j: j != 0, board[:,y])

def box(board, x, y):
	i = x // 3
	j = y // 3
	box = list(board[i * 3][j * 3 : (j + 1 ) * 3]) + \
		  list(board[i * 3 + 1][j * 3 : (j + 1 ) * 3]) + \
		  list(board[i * 3 + 2][j * 3 : (j + 1 ) * 3])
	return filter(lambda x: x != 0, box)


print solve(board)