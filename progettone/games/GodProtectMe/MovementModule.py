#Movement module

import pygame

def move_player_1(pos_x, pos_y, speed) -> tuple:
    """Gets the initial position and speed and returns the final position in the next frame
    """
    
    player_direction = pygame.Vector2(0, 0)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        player_direction.x = -1
        
    if keys[pygame.K_d]: 
        player_direction.x = 1
        
    if keys[pygame.K_w]: 
        player_direction.y = -1
            
    if keys[pygame.K_s]:
        player_direction.y = 1
    
    if player_direction.x != 0 and player_direction.y != 0:
        if player_direction.x == 1 and player_direction.y == 1:
            player_direction = pygame.Vector2(1 / (2 ** 1/2), 1 / (2 ** (1/2)))
        
        if player_direction.x == 1 and player_direction.y == -1:
            player_direction = pygame.Vector2(1 / (2 ** 1/2), -1 / (2 ** (1/2)))
        
        if player_direction.x == -1 and player_direction.y == 1:
            player_direction = pygame.Vector2(-1 / (2 ** 1/2), 1 / (2 ** (1/2)))
        
        if player_direction.x == -1 and player_direction.y == -1:
            player_direction = pygame.Vector2(-1 / (2 ** 1/2), -1 / (2 ** (1/2)))
    
    return player_direction.x * speed + pos_x, player_direction.y * speed + pos_y

def move_player_2(pos_x, pos_y, speed) -> tuple:
    """Gets the initial position and speed and returns the final position in the next frame
    """
    
    player_direction = pygame.Vector2(0, 0)
    
    if keys[pygame.K_LEFT]: 
        player_direction.x = -1
        
    if keys[pygame.K_RIGHT]: 
        player_direction.x = 1
        
    if keys[pygame.K_UP]: 
        player_direction.y = -1
            
    if keys[pygame.K_DOWN]:
        player_direction.y = 1
    
    if player_direction.x != 0 and player_direction.y != 0:
        if player_direction.x == 1 and player_direction.y == 1:
            player_direction = pygame.Vector2(1 / (2 ** 1/2), 1 / (2 ** (1/2)))
        
        if player_direction.x == 1 and player_direction.y == -1:
            player_direction = pygame.Vector2(1 / (2 ** 1/2), -1 / (2 ** (1/2)))
        
        if player_direction.x == -1 and player_direction.y == 1:
            player_direction = pygame.Vector2(-1 / (2 ** 1/2), 1 / (2 ** (1/2)))
        
        if player_direction.x == -1 and player_direction.y == -1:
            player_direction = pygame.Vector2(-1 / (2 ** 1/2), -1 / (2 ** (1/2)))
    
    return player_direction.x * speed + pos_x, player_direction.y * speed + pos_y


def is_on_screen(pos_x, pos_y, screen_width, screen_height) -> bool:
    """Given the coordinates of an object and the size of the screen, the function returns a bool that tells if the object is on screen
    """
    
    if pos_x < 0 or pos_x > screen_width:
        return False
    if pos_y < 0 or pos_y > screen_height:
        return False
    
    return True

def is_in_range(pos_x_1, pos_y_1, pos_x_2, pos_y_2, max_distance) -> bool:
    """Given the position of 2 objects and a max distance, the function returns a boolean telling if the objects are close enough to interact with eachother
    """
    
    distance_x = pos_x_1 - pos_x_2
    distance_y = pos_y_1 - pos_y_2
    
    distance_normal = ((distance_x ** 2) + (distance_y ** 2)) ** (1/2)
    
    if distance_normal > max_distance:
        return False
    if distance_normal <= max_distance:
        return True
