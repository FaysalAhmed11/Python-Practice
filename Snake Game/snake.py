import pygame
import time
import random

#initialize the pygame library
pygame.init()

color_1 = (255,255,255)#white
color_2 = (255,255,102)#yellow
color_3 = (0,0,0)#black
color_4 = (222,188,90)
color_5 = (0,255,0)#green
color_6 = (255,0,0)#red

box_len = 950
box_height = 600

caption = pygame.display.set_mode((box_len,box_height))
pygame.display.set_caption("Snake Game")

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10

display_style = pygame.font.SysFont("Times New Roman", 28, "bold")
score_font = pygame.font.SysFont("arial",35,"bold")

def final_score(score):
    value = score_font.render("Hey! Enjoy Your Game----> Score is: " +str(score), True, color_2)
    caption.blit(value, [0,0])
    
def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(caption, color_1, [x[0], x[1], snake_block])
        

def display_msg(msg, color):
    message = display_style.render(msg, True, color)
    caption.blit(message, [box_len/6, box_height/3])
    
def game_start():
    game_over = False
    game_close = False
    
    value_x1 = 