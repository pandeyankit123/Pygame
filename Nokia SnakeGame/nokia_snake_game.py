#Made by Ankit Pandey
#Dated: 25 September 2022

from json import load
from operator import truediv
from tkinter import font
import pygame
import random
import os

# pygame.mixer.init()
# pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play

pygame.init()

#colors 
white=(255, 255, 255)
red = (255, 0, 0)
black=(0, 0, 0)
green=(0, 255, 0)

#creating window
screen_width = 900
screen_height = 600
gameWindow=pygame.display.set_mode((screen_width, screen_height))

# #background Img
# bgimg = pygame.image.load("img.jpg")
# bgimg = pygame.transform.scale(bgimg, (screen_height, screen_height)).convert_alpha()

pygame.display.set_caption("Nokia Snake Game")
pygame.display.update()

clock=pygame.time.Clock()
font= pygame.font.SysFont(None, 55)

def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
def plot_snake(gameWindow, color, snk_list, snake_size):
    # print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

#welcome screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        text_screen("Welcome to Nokia Snake Game", white, 165, 250)
        text_screen("Press Space Bar to Play", white, 230, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(30)

#Game Loop
def gameloop():
    #Game specific variable
    exit_game = False
    game_over = False
    snake_x=35
    snake_y=60
    velocity_x=0
    velocity_y=0
    food_x=random.randint(20, screen_width-20)
    food_y=random.randint(20, screen_height-20)
    score=0
    init_velocity=5
    snake_size=10
    fps=30
    
    snk_list = []
    snk_length = 1
    #check if hiscore file exists
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore=f.read()

    while not exit_game:
        if game_over:     
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            # gameWindow.fill(black)
            text_screen("Game Over! Press Enter To Continue", white, screen_width/2 - 350, screen_height/2 -25)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and velocity_x==0:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT and velocity_x==0:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key == pygame.K_UP and velocity_y==0:
                        velocity_x=0
                        velocity_y=-init_velocity
                    if event.key == pygame.K_DOWN and velocity_y==0:
                        velocity_x=0
                        velocity_y=init_velocity
                    if event.key == pygame.K_SPACE:
                        score += 50

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y-food_y)<8:
                score+=10
                # print("Score: ",score*10)
                food_x=random.randint(50, screen_width-50)
                food_y=random.randint(130, screen_height- 90)
                snk_length +=5
                # print(hiscore)
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(black)
            # gameWindow.blit(bgimg, (0,0))
            
            pygame.draw.rect(gameWindow, white, [20, 48,  screen_width-40, screen_height-70])
            pygame.draw.rect(gameWindow, black, [22, 50,  screen_width-44, screen_height-74])

            text_screen("  Score: "+str(score) + "  Hiscore: "+ str(hiscore), green, 5, 5)

            pygame.draw.rect(gameWindow, white, [food_x, food_y, snake_size, snake_size])

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over=True

            if snake_x<26 or snake_x>screen_width-40 or snake_y<55 or snake_y>screen_height-40:
                game_over=True
                # print("Game Over")

            # pygame.draw.rect(gameWindow, red, [snake_x, snake_y,  snake_size, snake_size])
            plot_snake(gameWindow, red, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

# gameloop()

welcome()