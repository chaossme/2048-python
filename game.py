import tkinter, random
from variables import *

class game ():
	def __init__ (self, size = 4):

		self.size = size
		self.canvasWidth, self.canvasHeight, self.margin, self.tileMargin = 500, 500, 20, 10

		self.tileSizeR = ((self.canvasWidth - 2 * self.margin) / self.size) / 2

		self.canvas = tkinter.Canvas(
			width = self.canvasWidth,
			height = self.canvasHeight,
		)
		self.canvas.pack()

		self.fieldDict = {
			'startingPoint': (self.margin, self.margin),
			'endingPoint': (self.canvasWidth - self.margin, self.canvasHeight - self.margin),
		}

		self.field = self.canvas.create_rectangle(
			self.fieldDict['startingPoint'],
			self.fieldDict['endingPoint'],
			fill = '#bbada0',
			outline = '#bbada0',
		)

		self.grid = []

		# build empty grid
		for r in range(size):
			self.grid.append([])
			for s in range(size):
				self.grid[r].append([])
				self.buildTile((r, s), None)

		# init first 2 tiles
		randomTwosPositions = [
			(0,1),
			(0,2),
		]#[self.generateRandomPosition() for x in range(random.randint(1,2))]

		for pos in randomTwosPositions:
			self.buildTile(pos, 2)

		self.canvas.bind_all('<Right>', self.onRight)
		self.canvas.bind_all('<Left>', self.onLeft)
		self.canvas.bind_all('<Up>', self.onUp)
		self.canvas.bind_all('<Down>', self.onDown)

		self.canvas.mainloop()

	def onRight (self, event):
		
		# merge all possible tiles
		for x in range(self.size - 1, 0, -1):
			for y in range(self.size):

				currentPosition = (x, y)
				currentValue = self.getValue(currentPosition)
				toMergeTilePosition = None

				if currentValue == None:
					continue

				for _x in range(0, x):
					rnPosition = (_x, y)
					rnValue = self.getValue(rnPosition)

					if currentValue == rnValue:
						toMergeTilePosition = rnPosition
					elif rnValue != None:
						toMergeTilePosition = None

				if toMergeTilePosition != None:
					self.merge(toMergeTilePosition, currentPosition)

		for x in range(self.size - 2, -1, -1):
			for y in range(self.size):
				currentPosition = (x, y)
				currentValue = self.getValue(currentPosition)
				toMovePosition = currentPosition

				if currentValue == None:
					continue

				for _x in range(self.size - 1, x, -1):
					rnPosition = (_x, y)
					rnValue = self.getValue(rnPosition)

					if self.isReserved(rnPosition):
						toMovePosition = currentPosition
					elif toMovePosition == currentPosition:
						toMovePosition = rnPosition

				self.buildTile(currentPosition, None)
				self.buildTile(toMovePosition, currentValue)

		self.buildRandomTile()

	def onLeft (self, event):
		
		# merge all possible tiles
		for x in range(self.size - 1):
			for y in range(self.size):

				currentPosition = (x, y)
				currentValue = self.getValue(currentPosition)
				toMergeTilePosition = None

				if currentValue == None:
					continue

				for _x in range(self.size - 1, x, -1):
					rnPosition = (_x, y)
					rnValue = self.getValue(rnPosition)

					if currentValue == rnValue:
						toMergeTilePosition = rnPosition
					elif rnValue != None:
						toMergeTilePosition = None

				if toMergeTilePosition != None:
					self.merge(toMergeTilePosition, currentPosition)

		for x in range(1, self.size):
			for y in range(self.size):
				currentPosition = (x, y)
				currentValue = self.getValue(currentPosition)
				toMovePosition = currentPosition

				if currentValue == None:
					continue

				for _x in range(0, x):
					rnPosition = (_x, y)
					rnValue = self.getValue(rnPosition)

					if self.isReserved(rnPosition):
						toMovePosition = currentPosition
					elif toMovePosition == currentPosition:
						toMovePosition = rnPosition

				self.buildTile(currentPosition, None)
				self.buildTile(toMovePosition, currentValue)

		self.buildRandomTile()

	def onUp (self, event):
		
		# merge all possible tiles
		for y in range(0, self.size - 1):
			for x in range(self.size):

				currentPosition = (x, y)
				currentValue = self.getValue(currentPosition)
				toMergeTilePosition = None

				if currentValue == None:
					continue

				for _y in range(self.size - 1, y, -1):
					rnPosition = (x, _y)
					rnValue = self.getValue(rnPosition)

					if currentValue == rnValue:
						toMergeTilePosition = rnPosition
					elif rnValue != None:
						toMergeTilePosition = None

				if toMergeTilePosition != None:
					self.merge(toMergeTilePosition, currentPosition)

		for x in range(self.size):
			for y in range(1, self.size):
				currentPosition = (x, y)
				currentValue = self.getValue(currentPosition)
				toMovePosition = currentPosition

				if currentValue == None:
					continue

				for _y in range(0, y):
					rnPosition = (x, _y)
					rnValue = self.getValue(rnPosition)

					if self.isReserved(rnPosition):
						toMovePosition = currentPosition
					elif toMovePosition == currentPosition:
						toMovePosition = rnPosition

				self.buildTile(currentPosition, None)
				self.buildTile(toMovePosition, currentValue)

		self.buildRandomTile()

	def onDown (self, event):
		
		# merge all possible tiles
		for x in range(self.size):
			for y in range(self.size - 1, 0, -1):

				currentPosition = (x, y)
				currentValue = self.getValue(currentPosition)
				toMergeTilePosition = None

				if currentValue == None:
					continue

				for _y in range(0, y):
					rnPosition = (x, _y)
					rnValue = self.getValue(rnPosition)

					if currentValue == rnValue:
						toMergeTilePosition = rnPosition
					elif rnValue != None:
						toMergeTilePosition = None

				if toMergeTilePosition != None:
					self.merge(toMergeTilePosition, currentPosition)

		for x in range(self.size):
			for y in range(self.size - 2, -1, -1):
				currentPosition = (x, y)
				currentValue = self.getValue(currentPosition)
				toMovePosition = currentPosition

				if currentValue == None:
					continue

				for _y in range(self.size - 1, y, -1):
					rnPosition = (x, _y)
					rnValue = self.getValue(rnPosition)

					if self.isReserved(rnPosition):
						toMovePosition = currentPosition
					elif toMovePosition == currentPosition:
						toMovePosition = rnPosition

				self.buildTile(currentPosition, None)
				self.buildTile(toMovePosition, currentValue)

		self.buildRandomTile()

	def merge (self, fromPosition, toPosition):
		self.buildTile(fromPosition, None)
		self.buildTile(toPosition, self.getValue(toPosition) * 2)

	def getTileBackground (self, value):
		return tileColors[value]

	def getValue (self, position):
		return self.grid[position[0]][position[1]]['value']

	def isReserved (self, position):
		return self.getValue(position) != None

	def createTileObject (self, position = (0, 0), value = None):
		self.grid[position[0]][position[1]] = {
			'value': value,
		}

	def buildTile (self, position = (0, 0), value = 2):
		self.createTileObject(position, value)

		# stred kocky
		midpoint = (
			self.fieldDict['startingPoint'][0] + (self.tileSizeR * 2) * position[0] + self.tileSizeR,
			self.fieldDict['startingPoint'][1] + (self.tileSizeR * 2) * position[1] + self.tileSizeR,
		)

		backgroundColor = self.getTileBackground(value) # pozadie kocky podla hodnoty kocky

		self.canvas.create_rectangle(
			(midpoint[0] - self.tileSizeR, midpoint[1] - self.tileSizeR),
			(midpoint[0] + self.tileSizeR, midpoint[1] + self.tileSizeR),
			fill = backgroundColor,
			outline = backgroundColor,
			tag = 'tile{}'.format(str(position[1] * self.size + position[0])),
		)

		# pokial ma kocka hodnotu, vypis ju
		if value:
			self.canvas.create_text(midpoint, text = value)

	def generateRandomPosition (self):
		return (random.randint(0, self.size - 1), random.randint(0, self.size - 1))

	def buildRandomTile (self):

		emptyTiles = []

		for x in range(self.size):
			for y in range(self.size):
				if self.grid[x][y]['value'] == None:
					emptyTiles.append((x, y))

		# TODO: CHECK GAME OVER

		self.buildTile(random.choice(emptyTiles), 2)

game()