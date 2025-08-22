import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game 🐍")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (213, 50, 80)
green = (0, 255, 0)
blue  = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)


def score_display(score):
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [10, 10])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


game_loop()
