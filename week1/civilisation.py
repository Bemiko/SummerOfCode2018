#!/usr/bin/python3
import sys
import random

class Tile:
	IsOnLand = 0  # 0 - False, 1 - True
	ContinentLabel = 0

	def __init__(self, a):
		self.IsOnLand = a



class Map:
	MapHeight = 0
	MapWidth = 0	
	MatrixOfTiles = None 
	__SizeCounter = 0

	def __init__(self, a, b):
		self.MapWidth = a
		self.MapHeight = b 
		self.MatrixOfTiles = [[Tile(0) for h in range(0,self.MapHeight)] for w in range(0,self.MapWidth)]

	def RandomContinentsGenerator(self):
		for h in range(0,self.MapHeight):
			for w in range(0,self.MapWidth):
				self.MatrixOfTiles[w][h].IsOnLand = random.randrange(0, 2)

	def FindPointOnLand(self):
		px=random.randrange(0, self.MapWidth)
		py=random.randrange(0, self.MapHeight) 

		while (self.MatrixOfTiles[px][py].IsOnLand == 0):
			px=random.randrange(0, self.MapWidth)
			py=random.randrange(0, self.MapHeight) 
		return [px,py]

	def __LabelLandTileAndLandNeighbours(self, w, h, label): 
		if self.MatrixOfTiles[w][h].IsOnLand == 1 and self.MatrixOfTiles[w][h].ContinentLabel != label :
			self.__SizeCounter=self.__SizeCounter+1
			self.MatrixOfTiles[w][h].ContinentLabel = label
			if h > 0:
				self.__LabelLandTileAndLandNeighbours(w,h-1,label)
			if h < self.MapHeight - 1:
				self.__LabelLandTileAndLandNeighbours(w,h+1,label)
			if w > 0:
				self.__LabelLandTileAndLandNeighbours(w-1,h,label)
			if w < self.MapWidth - 1:
				self.__LabelLandTileAndLandNeighbours(w+1,h,label)
			if h > 0 and w > 0:
				self.__LabelLandTileAndLandNeighbours(w-1,h-1,label)
			if h > 0 and w < self.MapWidth - 1:
				self.__LabelLandTileAndLandNeighbours(w+1,h-1,label)
			if h < self.MapHeight - 1 and w > 0:
				self.__LabelLandTileAndLandNeighbours(w-1,h+1,label)
			if h < self.MapHeight - 1 and w < self.MapWidth - 1:
				self.__LabelLandTileAndLandNeighbours(w+1,h+1,label)

	def SizeOfContinent(self, coordinates): 
		label=0
		self.__LabelLandTileAndLandNeighbours(coordinates[0],coordinates[1],label)
		self.__SizeCounter=0
		label=1
		self.__LabelLandTileAndLandNeighbours(coordinates[0],coordinates[1],label)
		return self.__SizeCounter

	#
	def SizesOfAllContinents(self):
		for h in range(0,self.MapHeight):
			for w in range(0,self.MapWidth):
				self.MatrixOfTiles[w][h].ContinentLabel = 0

		Sizes=[] 
		label=1

		for h in range(0,self.MapHeight):
			for w in range(0,self.MapWidth):
				if self.MatrixOfTiles[w][h].IsOnLand==1 and self.MatrixOfTiles[w][h].ContinentLabel == 0 :
					self.__SizeCounter=0
					self.__LabelLandTileAndLandNeighbours(w,h,label)
					Sizes.append(self.__SizeCounter)
					label=label+1
		return Sizes


	def PrintMap(self):
		for w in range(0,self.MapWidth+2):
			sys.stdout.write('_')
		sys.stdout.write('\n')

		for h in range(0,self.MapHeight):
			sys.stdout.write('|')
			for w in range(0,self.MapWidth):
				
				if self.MatrixOfTiles[w][h].IsOnLand:
   					sys.stdout.write('X')
				else:
   					sys.stdout.write(' ')
			sys.stdout.write('| \n')

		for w in range(0,self.MapWidth+2):
			sys.stdout.write('-')
		sys.stdout.write('\n')

	def PrintContinents(self):
		for h in range(0,self.MapHeight):
			for w in range(0,self.MapWidth):
				if self.MatrixOfTiles[w][h].IsOnLand:
   					sys.stdout.write('['+str(self.MatrixOfTiles[w][h].ContinentLabel)+']')
				else:
   					sys.stdout.write('[ ]')
			sys.stdout.write('\n')



def main(a,b):
	

	OurMap = Map(a,b)
	print("Width of the map: "+str(OurMap.MapWidth))
	print("Height of the map: "+str(OurMap.MapHeight))

	OurMap.RandomContinentsGenerator()
	print("Map:  (X = Land)")	
	OurMap.PrintMap()

	point = OurMap.FindPointOnLand()
	print("Size of the labeled by 1 continent containing the point "+str(point)+" : "+str(OurMap.SizeOfContinent(point)))
	OurMap.PrintContinents()


	print("Sizes of all continents:") 
	print(OurMap.SizesOfAllContinents()) 
	print("Labeled continents:")
	OurMap.PrintContinents()


if __name__ == "__main__":
	if len(sys.argv) <= 2:
 		print("Usage of the script: python civilisation.py width height")
 		main(11,11)
	else:
		main(int(sys.argv[1]),int(sys.argv[2]))