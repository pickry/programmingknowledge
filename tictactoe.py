#                                              TIC TAC TOE
#the algorithm
'''
1. make the board draw lines and get images loaded
2. a function to get the result of the game which player won or if it was a draw
3. a function to print these results on game screen
4. drawing the X or O at the position choosen would contain two functions
    a.choosing the point using the mouse
    b. rendering the image at that box

WE HAVE THESE 5 FUNCTIONS THAT WE WOULD PUT TOGETHER TO MAKE THE THE TIC TAC TOE GAME
i. draw board function 
ii. get results printed use font
iii. check winning cases and strike the win line draw module
iv. get coordinates of mouse click use mouse module
v. put the picture at these coordinates
'''

import pygame 
pygame.init()

XO = 'X' #the initialised variable that stores whose turn it is

winner = None#to store the winner used in checkwin

draw = None#to see if it is a draw a boolean

board = [[None]*3, [None]*3, [None]*3] #the board is a matrix basically of size 3X3

clock = pygame.time.Clock()#the Clock object for framerate

screen = pygame.display.set_mode((400,400))#screen setup

pygame.display.set_caption("Tic Tac Toe")#the caption\

ximg = pygame.image.load("tictactoe/X.png")
oimg = pygame.image.load("tictactoe/O.png")#loaded images from the folder 

ximg = pygame.transform.scale(ximg, (80, 80))
oimg = pygame.transform.scale(oimg, (80, 80))#scaled both the images according to the size of one block available

def drawgrid(): #drawing the board with lines 	
	screen.fill((241, 192, 185))
	#two vertical and two horizontal lines are required to create a 3X3 grid
	pygame.draw.line(screen, (236, 248, 127), (400 / 3, 0), (400 / 3, 400), 6)#the first vertical line 
	pygame.draw.line(screen, (236, 248, 127), ((400 / 3) * 2, 0), ((400 / 3) * 2, 400), 6)#the second vertical line the coordinates of first line
	#are multiplied by 2

	pygame.draw.line(screen, (236, 248, 127), (0, 400 / 3), (400, 400 / 3), 6)#the first horizontal line
	pygame.draw.line(screen,(236, 248, 127), (0, (400 / 3) * 2), (400,(400 / 3) * 2), 6)#the second horizontal line
	

def result():#to get results and print them on screen
	global draw,winner
	if winner:
		message = winner + " won!"
	if draw:
		message = "Game Draw!"

	font = pygame.font.SysFont('Georgia', 70)
	text = font.render(message, 1, (24, 154, 180))	
	screen.fill ((0, 0, 0), (0, 400, 500, 100))
	text_rect = text.get_rect(center =(400 // 2, 400//2))
	screen.blit(text, text_rect)
	pygame.display.update()


def wincases(): #check the winner and draw a line across how the win was 
	global board, winner, draw
	# check all rows to find a winning row
	for row in range(0, 3):
		if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] != None)):
			winner = board[row][0]
			pygame.draw.line(screen, (250, 0, 0),(0, (row + 1)*400 / 3 -400 / 6),(400, (row + 1)*400 / 3 - 400 / 6 ),4)
			result()
			break

	# check all columns to find a winning column
	for col in range(0, 3):
		if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] != None)):
			winner = board[0][col]
			pygame.draw.line (screen, (250, 0, 0), ((col + 1)* 400 / 3 - 400 / 6, 0),((col + 1)* 400 / 3 - 400 / 6, 400), 4)
			result()
			break

	# check the two diagonals
	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != None):

		# the principle diagonal
		winner = board[0][0]
		pygame.draw.line (screen, (250, 70, 70), (50, 50), (350, 350), 4)
		result()

	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != None):

		# the other diagonal
		winner = board[0][2]
		pygame.draw.line (screen, (250, 70, 70), (350, 50), (50, 350), 4)
		result()
	#if the result is draw
	if(all([all(row) for row in board]) and winner == None ):
		draw = True
		result()
	

def getimg(row, col): #to render the image at the clicked position update value of xo as in whose turn it is 
	global board, XO

	#the first block is defined as posx
	if row == 1:
		posy = 30

	#the second block would be the after 1 block and 30 units as defined above
	if row == 2:
		posy = 400 / 3 + 30

	if row == 3:#the 3rd block would be after the second vertical line and 30 units
		posy = 400 / 3 * 2 + 30

	if col == 1:#similarly with y
		posx = 30

	if col == 2:
		posx = 400 / 3 + 30

	if col == 3:
		posx = 400 / 3 * 2 + 30

	#assigning the block on board its value
	board[row-1][col-1] = XO

	if(XO == 'X'):

		#if its X's turn put ximg and change it to O
		screen.blit(ximg, (posx, posy))
		XO = 'O'

	else:# and vice versa
		screen.blit(oimg, (posx, posy))
		XO = 'X'
	pygame.display.update()

def input_to_block(): #to get the position of the coordinate clicked so that you use the above function draw to get the respective sign at the clicked position
	#basically to find out which block is clicked on board
	# get coordinates of mouse click
	x, y = pygame.mouse.get_pos()

	#checking one by one the boundaries to give a definite coordinate
	if(x<400 / 3):#check if the click is within the first vertical line
		col = 1

	elif (x<400 / 3 * 2):#we would move to this case only if the above one is not appropriate 
		col = 2

	elif(x<400):
		col = 3

	else:
		col = None

	# similarly assing the row 
	if(y<400 / 3):
		row = 1

	elif (y<400 / 3 * 2):
		row = 2

	elif(y<400):
		row = 3

	else:
		row = None

	if(row and col and board[row-1][col-1] is None):
		global XO
		getimg(row, col)#put in the row and column determined
		wincases()#and check if the game is won by any player yet

drawgrid() #calling the function in the main part

while True: #the game loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			input_to_block()
			
	pygame.display.update()
	clock.tick(30)#refresh rate
