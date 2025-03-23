import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
PADDLE_SPEED = 8
BALL_SPEED_X, BALL_SPEED_Y = 4, -4

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paddle Ball Game")
clock = pygame.time.Clock()

# Paddle and Ball Initialization
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [BALL_SPEED_X, BALL_SPEED_Y]

def draw():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, paddle)
    pygame.draw.ellipse(screen, BLACK, ball)
    pygame.display.flip()

def move_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-PADDLE_SPEED, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(PADDLE_SPEED, 0)

def move_ball():
    global ball_speed
    ball.move_ip(ball_speed)
    
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]
    
    if ball.bottom >= HEIGHT:
        reset_game()

def reset_game():
    global ball_speed
    time.sleep(1)
    ball.topleft = (WIDTH // 2, HEIGHT // 2)
    ball_speed = [BALL_SPEED_X * random.choice([-1, 1]), BALL_SPEED_Y]

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        move_paddle()
        move_ball()
        draw()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
