#                                             THE SNAKE GAME
#THE ALGORITHM
'''
1. set the initial coordinates or start coordinates of the snake
2. The body of the snake should be a number of rectangles arranged consecutively their coordinates would be saved
   in a list
3. Also define the food position which would be randomly picked everytime the snake eats the food
4. To randomly pick a spot for the food we would import the random module
5. Keep track of the score and increase size of the snake everytime it eats the food
6. Define a game over function to end the game
7. Handle movement of the snake using key inputs (use key module)'''
import pygame
pygame.init()#imported and initialised pygame module

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Snake game!')#set up the screen and set up a caption

import time
import random#imported random for random coordinates for food


snake_pos = [80, 30]#initial or start position of snake
snake_speed = 10  #snake moves with this speed for making the game difficult increase this and play


clock = pygame.time.Clock()# object to set framerate later


snake_body = [[80, 30],[70, 30]] #snake's body

foodpos = [random.randrange(1, (600//10)) * 10, random.randrange(1, (500//10)) * 10] #first random spot of food

food = True #boolean to know when to change the food's position

score = 0# workin with score initial score is 0
def show_score(): #to display score just like text no calculation of score is done in this function
	font = pygame.font.SysFont('Georgia', 30)
	Font = font.render('Score : ' + str(score), True, 'pink')	
	rect = Font.get_rect()	
	screen.blit(Font, rect)#just like displaying text on screen


def game_over():#also to diplay the 'game over' text 
	font = pygame.font.SysFont('Georgia', 50)
	Font = font.render(
		'GAME OVER Score: ' + str(score), True, 'purple')
	rect = Font.get_rect()
	rect.midtop = (600/2, 500/4)
	screen.blit(Font, rect)
	pygame.display.flip()
	time.sleep(2)#to quit automatically when game over
	pygame.quit()
	quit()


#to handle movement of the snake
dir = 'RIGHT' #initial direction of movement of the snake before any input
next_dir = dir #the input given


while True: #the game loop covers actual movement handling, the game over conditions, the figure and score functions
	for event in pygame.event.get():#to know what key was pressed and where to go next
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				next_dir = 'UP'
			if event.key == pygame.K_DOWN:
				next_dir = 'DOWN'
			if event.key == pygame.K_LEFT:
				next_dir = 'LEFT'
			if event.key == pygame.K_RIGHT:
				next_dir = 'RIGHT'
	#HANDLING THE MOVEMENTS
	#updating dir with the input stored in next_dir
	if next_dir == 'UP' and dir != 'DOWN':
		dir = 'UP'
	if next_dir == 'DOWN' and dir != 'UP':
		dir = 'DOWN'
	if next_dir == 'LEFT' and dir != 'RIGHT':
		dir = 'LEFT'
	if next_dir == 'RIGHT' and dir != 'LEFT':
		dir = 'RIGHT'

	# to move the snake change its position 
	if dir == 'UP':
		snake_pos[1] -= 10
	if dir == 'DOWN':
		snake_pos[1] += 10
	if dir == 'LEFT':
		snake_pos[0] -= 10
	if dir == 'RIGHT':
		snake_pos[0] += 10

	
	snake_body.insert(0, list(snake_pos))#insert every coordinate that the snake passes through
	if snake_pos[0] == foodpos[0] and snake_pos[1] == foodpos[1]: # snake meets the food score is increases and it is time to set up a new food spot
		score += 10
		food = False
	else:#if snake doesnot meet the food then pop the coordinates 
		snake_body.pop()
		
	if not food:#if food is set false assign a new coordinate to foodpos
		foodpos = [random.randrange(1, (600//10)) * 10,random.randrange(1, (500//10)) * 10]
		
	food = True
	screen.fill('black')
	
	for pos in snake_body: #draw the snake
		pygame.draw.rect(screen, 'green',(pos[0], pos[1], 10, 10))
	pygame.draw.circle(screen, 'dark red', (foodpos[0], foodpos[1]),5)
	
	#THE GAME OVER CONDITIONS
	if snake_pos[0] < 0 or snake_pos[0] > 600-10:#bumped into the left or right wall
		game_over()
	if snake_pos[1] < 0 or snake_pos[1] > 500-10:#bumped into the upper or bottom wall
		game_over()
	for block in snake_body[1:]:#snake bites itself
		if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
			game_over()

	show_score()#see score all the time on screen

	pygame.display.update()
	clock.tick(snake_speed)
