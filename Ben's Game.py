import pygame, sys, time, random
from pygame.locals import *

pygame.init()

#create the display screen
display_w = 800
display_h = 600
screen = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Ben Game")

# Color definitions
black = (0, 0, 0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)

clock = pygame.time.Clock()

benImg = pygame.image.load('images/bensFace.png')

ben_w = 60

# define the player character
def ben(x, y):
	screen.blit(benImg, (x, y))

# define the falling grades, rectangles for now, later, letters and shit.
def grades(grade_x, grade_y, grade_w, grade_h, color):
        pygame.draw.rect(screen, color, [grade_x, grade_y, grade_w, grade_h])

# Displays a message on screen and restarts the game
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_w/2),(display_h/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

# displays the message "You Failed" and restarts the game
def collision():
        message_display("You Failed")

# creates a text surface so that we can display messages
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# calculates the current GPA based on the number of dodges
def calc_gpa(count):
        return count/5

# create the GPA counter
def print_gpa(gpa):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Current GPA: " + str(gpa), True, black)
        screen.blit(text,(0,0))
        
# define the main game loop
def game_loop():
        #set initial conditions for Ben
        x = display_h * 0.6
        y = display_h * 0.7
        x_change = 0
        ben_speed = 10


        # define the initial cond's for the grades
        grade_start_x = random.randrange(0, display_w)
        grade_start_y = -600
        grade_speed = 7
        grade_w = 100
        grade_h = 100
        color = green

        grade_count = 1
        dodged = 0
        
        # Start running the loop
        game_running = True
        
        while game_running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                game_running = False
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT or event.key == K_a:
                                        x_change = -ben_speed
                                elif event.key == pygame.K_RIGHT or event.key == K_d:
                                        x_change = ben_speed
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                        x_change = 0

                # generate Ben's movement
                x += x_change

                # fill the screen with a white background
                screen.fill(white)

                # generate grades movement and draw grades and Ben
                grades(grade_start_x, grade_start_y, grade_w, grade_h, color)
                grade_start_y += grade_speed
                ben(x,y)

                gpa = calc_gpa(dodged)
                print_gpa(gpa)
                if gpa >= 4:
                        message_display("GRAD SCHOOL")
                        time.sleep(2)
                        color = yellow
                        

                # set the boundaries at the sides of the screen.  
                if x > display_w - ben_w or x < 0:
                        collision()
                        
                # make the grades dispear at the bottom of the screen and have a new one reappear at the top.
                if grade_start_y > display_h:
                    grade_start_y = 0 - grade_h
                    grade_start_x = random.randrange(0,display_w)
                    dodged += 1
                    grade_speed += 1
                    grade_w += (dodged * 1.2)
                    ben_speed += 0.4

                # create the collision sequence for the grades
                if y < grade_start_y + grade_h and y > grade_start_y:
                        if (x > grade_start_x) and (x < grade_start_x + grade_w) or (x + ben_w > grade_start_x) and (x + ben_w < grade_start_x + grade_w):
                                collision()
                                
                #update the screen and draw the objects (30 fps)
                pygame.display.update()
                clock.tick(30)
        ### End While() ###

        ### Add protocol to exit the game when the x button is pushed ###
        pygame.quit()
        sys.exit()
### End Gameloop() ###

#start game
game_loop()







