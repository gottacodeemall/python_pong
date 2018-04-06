import pygame
import random
import sys
pygame.init()

def get_new_position(pos,val):
	newpos=(pos[0]+val[0],pos[1]+val[1])
	return newpos

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)


BLACK= (0,0,0)
RED = (255,0,0)
WHITE=(255,255,255)
SCREEN_SIZE=   SCREEN_WIDTH,SCREEN_HEIGHT= (900,600);
screen = pygame.display.set_mode(SCREEN_SIZE);

ball_centre = (SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
ball_radius = 20
ball = pygame.draw.circle(screen, RED, ball_centre, ball_radius)

PADDLE_LENGTH = 100
PADDLE_WIDTH = 10

paddle1_top = (5, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
paddle1_bottom = (5, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
paddle2_top = (SCREEN_WIDTH-PADDLE_WIDTH, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
paddle2_bottom = (SCREEN_WIDTH-PADDLE_WIDTH, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))


ball_velocity = (3,3)
paddle1_velocity=(0,0)
paddle2_velocity=(0,0)
pygame.display.update()
text = myfont.render('END GAME', False, (0, 0, 0))
flag =0
while True :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				paddle2_velocity = (0,-3)   
			elif event.key == pygame.K_DOWN:
				paddle2_velocity = (0,3)
			elif event.key == pygame.K_w:
				paddle1_velocity = (0,-3)    #Fill in the right values
			elif event.key == pygame.K_s:
				paddle1_velocity = (0,3)	
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or pygame.K_DOWN:
				paddle2_velocity = (0,0)	
				paddle1_velocity = (0,0)
	if(flag==1):
		continue
	paddle2_top = get_new_position(paddle2_top, paddle2_velocity)
	paddle2_bottom = get_new_position(paddle2_bottom, paddle2_velocity)
	paddle1_top = get_new_position(paddle1_top, paddle1_velocity)
	paddle1_bottom = get_new_position(paddle1_bottom, paddle1_velocity)
	if(paddle1_bottom[1]>SCREEN_HEIGHT):
		paddle1_bottom=(paddle1_bottom[0], SCREEN_HEIGHT)
		paddle1_top=(paddle1_top[0], SCREEN_HEIGHT-PADDLE_LENGTH)
	elif(paddle1_top[1]<0):
		paddle1_top=(paddle1_top[0], 0)	
		paddle1_bottom=(paddle1_bottom[0], PADDLE_LENGTH)
	if(paddle2_bottom[1]>SCREEN_HEIGHT):
		paddle2_bottom=(paddle2_bottom[0], SCREEN_HEIGHT)
		paddle2_top=(paddle2_top[0], SCREEN_HEIGHT-PADDLE_LENGTH)
	elif(paddle2_top[1]<0):
		paddle2_bottom=(paddle2_bottom[0], PADDLE_LENGTH)
		paddle2_top=(paddle2_top[0], 0)	
	screen.fill(BLACK)

	ball_centre=get_new_position(ball_centre,ball_velocity)
	if(ball_centre[0]-ball_radius<=PADDLE_WIDTH):
		print "yo"
		print ball_centre, paddle1_top, paddle1_bottom
		if(ball_centre[1]>=paddle1_top[1] and ball_centre[1]<=paddle1_bottom[1]):
			ball_velocity=(-1*ball_velocity[0],ball_velocity[1])
			ball_centre=get_new_position(ball_centre,ball_velocity)
		else:
			textrect=text.get_rect();
			textrect.centerx=text.get_rect().centerx
			textrect.centery=text.get_rect().centery
			screen.fill(WHITE)
			screen.blit(text,(0,0))
			pygame.display.update()
			flag=1;
			continue;	
	elif(ball_centre[0]+ball_radius>=SCREEN_WIDTH-PADDLE_WIDTH):
		print "yeah"
		print ball_centre, paddle2_top, paddle2_bottom
		if(ball_centre[1]>=paddle2_top[1] and ball_centre[1]<=paddle2_bottom[1]):
			ball_velocity=(-1*ball_velocity[0],ball_velocity[1])
			ball_centre=get_new_position(ball_centre,ball_velocity)
		else:
			textrect=text.get_rect()
			textrect.centerx=screen.get_rect().centerx
			textrect.centery=screen.get_rect().centery
			screen.fill(WHITE)
			screen.blit(text,textrect)
			pygame.display.update()
			flag=1;
			continue;
	if(ball_centre[1]+ball_radius>SCREEN_HEIGHT):
		ball_velocity=(ball_velocity[0],-1*ball_velocity[1])
		ball_centre=get_new_position(ball_centre,ball_velocity)
	elif(ball_centre[1]-ball_radius<0):
		ball_velocity=(ball_velocity[0],-1*ball_velocity[1])
		ball_centre=get_new_position(ball_centre,ball_velocity)	
	# if(ball_centre[0]+ball_radius>SCREEN_WIDTH):
	# 	ball_velocity=(-1*ball_velocity[0],ball_velocity[1])
	# 	ball_centre=(ball_centre[0]-ball_radius,ball_centre[1])
	# elif(ball_centre[0]+ball_radius<0):
	# 	ball_velocity=(-1*ball_velocity[0],ball_velocity[1])
	# 	ball_centre=(ball_radius,ball_centre[1])		
	paddle1=pygame.draw.line(screen,RED,paddle1_top,paddle1_bottom,PADDLE_WIDTH)
	paddle2=pygame.draw.line(screen,RED,paddle2_top,paddle2_bottom,PADDLE_WIDTH)
	ball=pygame.draw.circle(screen, RED, ball_centre, ball_radius)
	pygame.time.Clock().tick(60)
	pygame.display.update()