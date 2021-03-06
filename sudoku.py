import numpy as np

class Node:
	def __init__(self, x, y, value, level):
		self.x = x
		self.y = y
		self.value = value
		self.level = level

	def children(self):
		x = self.level // 9
		y = self.level % 9
		nodes = []
		values = possible_values(board, x, y)
		values.reverse()
		for i in values:
			nodes.append(Node(x, y, i, self.level + 1))
		return nodes

def solve(board):
	stack = []
	start = Node(0, -1, 0, 0)
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
	row = [i for i in values if i not in get_row(board, x)]
	column = [j for j in values if j not in get_column(board, y)]
	box = [k for k in values if k not in get_3_by_3(board, x, y)]
	return list(set(row) & set(column) & set(box))

def get_row(board, x):
	return filter(lambda x: x != 0, board[x])

def get_column(board, y):
	return filter(lambda x: x != 0, board[:,y])

def get_3_by_3(board, x, y):
	i = x // 3 * 3
	j = y // 3 * 3
	box = list(board[i + 0][j : j + 3]) + \
		  list(board[i + 1][j : j + 3]) + \
		  list(board[i + 2][j : j + 3])
	return filter(lambda x: x != 0, box)



# initialize board
board = np.array([[0 for x in range(9)] for x in range(9)])

# input given positions
n = int(raw_input()[0])

positions = []
for i in range(n):
	x, y, m = map(int, raw_input().split())
	positions.append((x - 1, y - 1))
	board[x - 1][y - 1] = m

# solve the puzzle
print solve(board)