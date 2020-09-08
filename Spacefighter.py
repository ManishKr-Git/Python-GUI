import pygame
import random
import time

# pygame initialization
pygame.init()

# create screen
win = pygame.display.set_mode((550, 600))
score = 0
font = pygame.font.SysFont("freesansbold.ttf", 32)

# pygame Caption and Icon
pygame.display.set_caption("Space Fighter")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


# draw the shooter
def drawShooter(icon, x, y):
	win.blit(icon, (x, y))


# Function to draw enemy
def drawEnemy(icon, x, y):
	win.blit(icon, (x, y))


# Function to draw bullet
def drawBullet(icon, x, y):
	win.blit(icon, (x, y))


def drawScore(scoer):
	score_font = font.render(f"Score:{score}", True, (255, 255, 255))
	win.blit(score_font, (10, 2))


def drawGame_over():
	font = pygame.font.SysFont("freesansbold.ttf", 80)
	final_font = font.render("Game Over", True, (255, 255, 0))
	win.blit(final_font, (150, 220))


# Enemy
enemy = pygame.image.load('enemy.png')
enemy_x = random.sample(range(15, 490, 46), 10)
enemy_y = random.sample(range(5, 200, 5), 10)
total_enemy = 10
enemy_dx = [1] * 10
enemy_dy = [0] * 10

# Shooter
shooter = pygame.image.load('shooter.png')
shooter_x = 250
shooter_y = 525
change_x = 0

# background image
back = pygame.image.load('background.png')
back = pygame.transform.scale(back, (550, 600))

# Bullet
bullet = pygame.image.load('bullet.png')
fire = False
bullet_x = []
bullet_y = []
bullet_count = 0

# main game_loop
game_over = False
while not game_over:
	for events in pygame.event.get():
		if events.type == pygame.QUIT:
			pygame.quit()
		if events.type == pygame.KEYDOWN:
			if events.key == pygame.K_RIGHT:
				change_x = 2
			elif events.key == pygame.K_LEFT:
				change_x = -2
			elif events.key == pygame.K_SPACE:
				bullet_count += 1
				bullet_x.append(shooter_x + 15)
				bullet_y.append(shooter_y - 20)
		if events.type == pygame.KEYUP:
			if events.key in [pygame.K_LEFT, pygame.K_RIGHT]:
				change_x = 0
	shooter_x += change_x
	if shooter_x < 5:
		shooter_x = 5
	elif shooter_x > 480:
		shooter_x = 480
	win.blit(back, (0, 0))

	# Drawing Bullets
	for c in range(bullet_count):
		drawBullet(bullet, bullet_x[c], bullet_y[c])
	bullet_y = [i - 2 for i in bullet_y]

	# drawing Enemies
	for e in range(total_enemy):
		drawEnemy(enemy, enemy_x[e], enemy_y[e])
	drawShooter(shooter, shooter_x, shooter_y)

	# drawingScore
	drawScore(score)

	# Check for collision
	counter = 0
	while counter < bullet_count:
		for e in range(total_enemy):
			if (enemy_x[e] + 50 > bullet_x[counter] > enemy_x[e] - 10) and enemy_y[e] < bullet_y[counter] < enemy_y[
				e] + 64:
				enemy_x[e] = random.randrange(20, 100)
				enemy_y[e] = random.randrange(5, 100)
				del bullet_x[counter]
				del bullet_y[counter]
				bullet_count -= 1
				score += 1
				drawScore(score)
				break
		counter += 1

	# Check for Game Over
	for e in range(total_enemy):
		if enemy_y[e] + 64 > 525:
			game_over = True

	counter = 0
	for counter in range(total_enemy):
		enemy_x[counter] = enemy_x[counter] + enemy_dx[counter]
	for e in range(total_enemy):
		if enemy_x[e] > 490 or enemy_x[e] < 10:
			enemy_dx[e] *= -1
			enemy_y[e] += 80
	pygame.display.update()
win.blit(back, (0, 0))
drawGame_over()
drawScore(score)
pygame.display.update()
time.sleep(2)
