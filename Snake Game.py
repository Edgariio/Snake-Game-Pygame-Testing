import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

screen_width = 800
screen_height = 600
snake_width = 10
snake_speed = 30

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Times New Roman", 30)
clock = pygame.time.Clock()


def game_loop():
    x = screen_width // 2
    y = screen_height // 2

    score = 0

    snake_body = []

    length_snake = 1

    x_change = 0
    y_change = 0

    x_food = random.randrange(0, screen_width, snake_width)
    y_food = random.randrange(0, screen_height, snake_width)

    close_game = False
    game_over = False

    while not close_game:
        while game_over:
            screen.blit(font.render("Game over, press p to play again or q to quit.", True, red),
                        [screen_width / 6, screen_height / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_loop()
                    elif event.key == pygame.K_q:
                        game_over = False
                        close_game = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_width
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_width
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_width
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_width
        x += x_change
        y += y_change
        screen.fill(white)
        snake_head = [x, y]

        snake_body.append(snake_head)
        if len(snake_body) > length_snake:
            del snake_body[0]

        for snake_block in snake_body[:-1]:
            if snake_block == snake_head:
                game_over = True

        for snake_part in snake_body:
            pygame.draw.rect(screen, red, [snake_part[0], snake_part[1], snake_width, snake_width])

        pygame.draw.rect(screen, green, [x_food, y_food, snake_width, snake_width])
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_over = True
        if x_food == x and y_food == y:
            score += 1
            x_food = random.randrange(0, screen_width, snake_width)
            y_food = random.randrange(0, screen_height, snake_width)
            length_snake += 1
        screen.blit(font.render("Score"+":"+" "+str(score), True, red), [10, 10])
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()