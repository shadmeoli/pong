# simple pygame game
import os, sys

import pygame
# initilizing dependancies
pygame.init()

import time


# params and constants
# screen oriantation
WIDTH, HEIGHT = 700, 500


# display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong    -- github@shadmeoli --")

# frame rate
FPS = 60

SCREEN_BG = (1, 4, 15)
SCREEN_WIDGETS = (21, 24, 35)
BREAKER = (21, 24, 35)
BALL_RADIUS = 10
BALL_COLOR = (255, 255, 255)

PADDLE_WIDHT ,PADDLE_HEIGHT = 20, 100


# paddles
class Paddle:
	SCREEN_WIDGETS = (121, 124, 135)
	VEL = 5

	def __init__(self, x,y ,width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height


	def draw(self, win):
		pygame.draw.rect(
			win, self.SCREEN_WIDGETS, (self.x, self.y, self.width, self.height))

	def move(self, up=True):
		if up:
			self.y -= self.VEL
		else:
			self.y += self.VEL


class Ball:
	MAX_VEL = 3

	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
		self.x_vel = self.MAX_VEL
		self.y_vel = 0


	def draw(self, win):
		pygame.draw.circle(win, BALL_COLOR, (self.x, self.y), BALL_RADIUS)


	def move(self):
		self.x += self.x_vel
		self.y += self.y_vel

# window drawing
def draw(win, paddles, ball):
	# coloring the bg
	win.fill(SCREEN_BG)

	for paddle in paddles:
		paddle.draw(win)


	pygame.draw.rect(win, BREAKER, (WIDTH//2 - 5, 0, 10, HEIGHT))

	ball.draw(win)

	pygame.display.update()


def collision(ball, left_pad, right_pad):

	if ball.y + ball.radius >= HEIGHT:
		ball.y_vel *= -1
	elif ball.y - ball.radius <= 0:
		ball.y_vel *= -1



	if ball.x_vel < 0:
		if ball.y >= left_pad.y and ball.y <= left_pad.y + left_pad.height:
			if ball.x - ball.radius <= left_pad.x + left_pad.width:
				ball.x_vel *= -1

				middle_y = left_pad.y + left_pad.height/2
				diff_in_y = middle_y - ball.y
				reduction = (left_pad.height/2) / ball.MAX_VEL
				y_vel = diff_in_y / reduction
				ball.y_vel =  -1 * y_vel

	else:
		if ball.y >= right_pad.y and ball.y <= right_pad.y + right_pad.height:
			if ball.x + ball.radius >= right_pad.x:
				ball.x_vel *= -1

				middle_y = right_pad.y + right_pad.height/2
				diff_in_y = middle_y - ball.y
				reduction = (right_pad.height/2) / ball.MAX_VEL
				y_vel = diff_in_y / reduction
				ball.y_vel = -1 * y_vel
		

def handle_movements(keys, left_pad, right_pad):
	# player 1 controlls
	if  keys[pygame.K_w] and left_pad.y - left_pad.VEL >= 0:
		left_pad.move(up=True)
	if  keys[pygame.K_s] and left_pad.y + left_pad.VEL + left_pad.height <= HEIGHT:
		left_pad.move(up=False)

	# player 2 controlles
	if  keys[pygame.K_UP] and right_pad.y - right_pad.VEL >= 0:
		right_pad.move(up=True)
	if  keys[pygame.K_DOWN] and right_pad.y + right_pad.VEL + right_pad.height <= HEIGHT:
		right_pad.move(up=False)

# screen
def main():
	run = True
	clock = pygame.time.Clock()

	# positioning the paddles perfectly at the center
	left_pad = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDHT, PADDLE_HEIGHT)
	right_pad = Paddle(WIDTH - 10 - PADDLE_WIDHT, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDHT, PADDLE_HEIGHT)

	ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)


	# placing the initlizer in a while loop
	while run:

		# optimizing the FPS
		clock.tick(FPS)

		draw(WIN, [left_pad, right_pad], ball)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break


		# users keboard signals
		keys = pygame.key.get_pressed()

		handle_movements(keys, left_pad, right_pad)

		ball.move()
		collision(ball, left_pad, right_pad)


	pygame.quit()



# running the initlizer from main screen function
if __name__ == '__main__':
	main()