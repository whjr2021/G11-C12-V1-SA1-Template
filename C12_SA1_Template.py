# Import "pygame", "time" and "random" modules 
import pygame
import time
import random

# Initialize "pygame"
pygame.init() 

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

# Create a "carx", "cary" and "bgy" variables to track car and background positions
carx = 140
cary = 450
bgy = 0
# Create a variable "threshold" and set its value to zero
threshold = 0

# Create a counter variable to keep track of gameloop iterations
counter = 0

# Choose random x and y locations for stone placement
stone_x = random.randint(100, carx+100)
stone_y = random.randint(100, cary-100)

# Student Activity 1-Step 1: Create a "red_carx", "red_cary" to track red car position. 
# Position the red car at (305, 200) location to begin with.
# 1. Assign the value 305 to "red_carx" variable

# 2. Assign the value 200 to "red_cary" variable


# Game loop
carryOn = True
# Create first time point "t1" 
t1 = time.time()
while carryOn:
    # NOTE: The images file and .py file in which image is being used must be in same folder
    
    # Display the background image
    bgImg_name = "road.png"
    bgImg = pygame.image.load(bgImg_name).convert_alpha()
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    screen.blit(bgImg_scaled,(0,0))
    
    # Display the yellow car image
    yellow_car_name = "yellow_car.png"
    yellow_car = pygame.image.load(yellow_car_name).convert_alpha()
    yellow_car_scaled = pygame.transform.smoothscale(yellow_car,(230,140))
    
    # Display the stone image
    stone_name = "stone.png"
    stone = pygame.image.load(stone_name).convert_alpha()
    stone_scaled = pygame.transform.smoothscale(stone,(70,60))
    
    # Display the red car image
    red_car_name = "red_car.png"
    red_car = pygame.image.load(red_car_name).convert_alpha()
    red_car_scaled = pygame.transform.smoothscale(red_car,(80,130))
    
    # Check for up, down, left, right, spacebar and enter key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False              
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cary -= 10
                bgy -= 10
            if event.key == pygame.K_DOWN:
                cary += 10
                bgy += 10
            if event.key==pygame.K_RIGHT:
                if carx <= 320:
                    carx += 10
            if event.key==pygame.K_LEFT:
                if carx >= 50:                          
                    carx -= 10 
            if event.key == pygame.K_SPACE:
                if carx < 260: 
                    carx += 90
            if event.key == pygame.K_RETURN:
                if game_time >= threshold and game_time <= (threshold+10):
                    cary -= 50 
                    threshold += 10
                
    # Reset car and backgroun positions
    if cary <= 30:
        bgy = 0
        cary = 450
        # Increment counter and print the "counter" variable value 
        # Everytime car position is reset increment counter by 1
        counter += 1 
        # Print the number of gameloop iterations completed.
        print("Number of gameloop iterations completed= ", counter)
        # Update the stone's x and y locations after incrementing the counter 
        stone_x = random.randint(100, carx+100)
        stone_y = random.randint(100, cary-100)
        
    # Create rectangle for car and stone
    yellow_car_rect = yellow_car_scaled.get_rect(topleft = (carx+75,cary))
    yellow_car_rect.width = yellow_car_rect.width/3
    stone_rect = stone_scaled.get_rect(topleft = (stone_x, stone_y))
    # Draw rectangles for car and stone
    pygame.draw.rect(screen,(100,0,100),yellow_car_rect)
    pygame.draw.rect(screen,(0,0,100),stone_rect)
    
    # Student Activity 1-Step 2: Get rectangle for red car
    # 1. Create a rectangle of red car image and store in "red_car_rect"

    # 2: Draw the "red_car_rect" on screen in light blue color with rgb combination (23,0,250) 

    
    # If car and stone rectangles collide, set car position to its initial position
    if yellow_car_rect.collidepoint(stone_rect.x,stone_rect.y):
        cary = 450
        stone_x = random.randint(100, carx+100)
        stone_y = random.randint(100, cary-100)
    
    # Student Activity 1-Step 3: Yellow and red car collision detection 
    # 1. Check if yellow and red cars collide

        # 2: Reset yellow car's position to carx=140, cary=450


        # 3: Reset red car's y position to red_cary=450 

    
        
    # Display yellow car image upon updating "carx" and "cary" variable values
    screen.blit(yellow_car_scaled,(carx, cary))
    
    # Display the stone upon updating "stone_x" and "stone_y" variable values  
    screen.blit(stone_scaled,(stone_x, stone_y))
    
    # Display red car image upon updating "red_carx" and "red_cary" variable values
    screen.blit(red_car_scaled,(red_carx, red_cary))
    
    # Create second time point "t2" 
    t2 = time.time()
    game_time = t2-t1
    game_time = round(game_time, 2)
    
    # Display game time elapsed
    font = pygame.font.Font(None, 35)
    text = font.render("TIME ELAPSED: " + str(game_time)+ "seconds", 1, (0, 255,255))
    screen.blit(text, (130,15))
    
    # Display finish line after 5 iterations of game loop
    # Check if "counter" is equal to 5
    if counter == 5:
        # Create and draw the finish line white-colored rectangle at (x,y)=(95, 40) with width=400 and height=30
        finish_line = pygame.Rect(95,40,400,30)
        pygame.draw.rect(screen,(255,255,255),finish_line)
        # Display "----------FINISH----------" text in a color with rgb combination as (255,0,0)
        font = pygame.font.Font(None, 40)
        text = font.render("----------FINISH----------", 1,(255,0,0))
        screen.blit(text, (160,45))
        pygame.display.flip()
        
        # End the game loop after displaying finish line
        pygame.time.wait(3000)
        screen.fill((0,100,200))
        font = pygame.font.Font(None, 40)
        # Display finish time in seconds text
        text1 = font.render("Finish time: " + str(round(game_time,2))+ " seconds", 1,(255,255,255))
        screen.blit(text1, (140,200))
        # Display "Game Over, Good Luck Next Time!" text
        text2 = font.render("Game Over, Good Luck Next Time!", 1,(255,255,255))
        screen.blit(text2, (80,250))
        pygame.display.flip()
        pygame.time.wait(5000)
        # Break out of 'while' game loop
        break
    
    # Update the contents of the display
    pygame.display.flip()
    
# On the occurence of "pygame.QUIT" event close the game screen.
pygame.quit()