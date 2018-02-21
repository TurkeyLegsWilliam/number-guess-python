import random

class GuessGame(object):
	"""Guessing Game"""
	
	def __init__(self):
		self.number = random.randint(0,10)
		self.players = []
		
	def startGame(self, numPlayers):
		# create list of players
		
		for i in range(0, numPlayers):
			s = Player()
			self.players.append(s)
			
		for i in range(0, 1000):
			for j in range(0, numPlayers):
				# prints old, asks for guess then verifies
				print("------------------------------------------")
				print("---Player %s---" % (j+1))
				print("Current Guess:", (self.players[j]).number)
				
				# prompt for input and check whether correct
				(self.players[j]).number = (self.players[j]).guess()
				if (self.players[j]).number == self.number:
					print("\nYou guessed right! The number is %s\n" % self.number)
					return True
				else:
					print("\nWRONG!\n")
				
				
		return False # game did not complete		

class Player(object):
	""" Player object"""
	def __init__(self):
		self.number = -1 # guessed number
	
	def guess(self):
		playerGuessNum = -1
		while True:
			playerGuessNum = input("Enter Guess: ")
			playerGuessNum = int(playerGuessNum)
			
			# check
			if playerGuessNum >= 0 and playerGuessNum <= 9:
				break
				
			print("INVALID INPUT: must be from 0 through 9")
			
		return playerGuessNum


#initialize game
game1 = GuessGame()

# asks for number of players
while True:
	numberPlayers = int(input("Enter number of players:"))
	if numberPlayers >= 1:
		break
	
	print("INVALID INPUT: must be greater or equal to 1")

gameFinished = game1.startGame(numberPlayers)

if gameFinished == False:
	print("Game did not finish.")
else:
	print("Game over.")