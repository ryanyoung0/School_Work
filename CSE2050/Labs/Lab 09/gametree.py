# Here is the board class; it has two attributes, knight and pawns; each piece is a pair of numbers between 0 and 7
class Board:
	def __init__(self, pieces):
		self.knight = pieces[0]
		self.pawns = pieces[1:]

	# prints board as 8 strings, 1 per line, with optional heading
	def printBoard(self, heading=""):
		if (heading):
			print(heading)
		board = [" - - - - - - - -"]*8
		(x,y) = self.knight
		row = board[x]
		board[x] = row[0:2*y+1] + "X" + row[2*y+2:]
		for (x,y) in self.pawns:
			row = board[x]
			board[x] = row[0:2*y+1] + "o" + row[2*y+2:]
		for row in board[:]:
			print(row)

	# returns list of knight moves that will eat a pawn, if any
	def findGoodMoves(self):
		(x0, y0) = self.knight
		moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
		goodMoves = []
		for (x, y) in moves:
			(x1, y1) = (x0 + x, y0 + y)
			#print ("trying move ", x, y)
			if (x1, y1) in self.pawns:
				goodMoves += [(x, y)]
		return goodMoves

	# returns a new board that's a copy of this one
	def copyBoard(self):
		newBoard = Board([self.knight]+self.pawns)
		return newBoard

	#given a board and a move, compute the next board
	def applyMove(self, move):
		(x0, y0) = self.knight
		(x, y) = move
		if ((x0 + x) >= 0 and (y0 + y) >= 0) and ((x0 + x) < 8 and (y0 + y) < 8):
			self.knight = (x0 + x, y0 + y)
			if self.knight in self.pawns:
				self.pawns.remove(self.knight)
			return True
		else:
			return False

	## Part 1
	def printGoodMovesBoard(self):
		gm = self.findGoodMoves()
		for i in gm:
			copy = self.copyBoard()
			copy.applyMove(i)
			loc = "Board with move " + str(copy.knight)
			copy.printBoard(loc)

	def printAllMovesBoard(self):
		AM = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
		for i in AM:
			copy = self.copyBoard()
			(x , y) = (i[0] + copy.knight[0], i[1] + copy.knight[1])
			loc = "Board with move " + str((x, y))
			if copy.applyMove(i) == True:
				copy.printBoard(loc)
			else:
				print ("Invalid move: " + str((x, y)))
## Part 2
def dfsCapture(board):
	if len(board.pawns) == 0:
		return True
	gm = board.findGoodMoves()
	sum = 0
	while sum < len(gm):
		if board.applyMove(gm[sum]) == True:
			sum += 1
			if sum == len(gm) - 1:
				return True
		return False


def bfsCapture(board):
	gm = board.findGoodMoves()
	for i in gm:
		if len(board.pawns) == 0:
			return True
		elif board.applyMove(i) == True:
			return True
		return False


## Part 3
def findPath(board, path = []):
	if path == []:
		path = [board.knight]
	gm = board.findGoodMoves()
	if len(board.pawns) == 0:
		gm = None
		return path
	elif gm != []:
		for i in gm:
			board.applyMove(i)
			path.append(board.knight)
			gm = None
			return findPath(board, path)
	else:
		gm = None
		return []
## Part 4
def findAllPaths(board, path=[]):
	lst = []
	queue = [(board, [board.knight])]
	while queue != []:
		(x, ml) = queue.pop()
		if x.pawns == []:
			lst.append(ml)
		msl = x.findGoodMoves()
		for i in msl:
			copy = x.copyBoard()
			copy.applyMove(i)
			queue.insert(0, (copy,ml + [copy.knight]))
	return lst
