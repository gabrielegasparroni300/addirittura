#Movement module

import pygame

def move_player_1(pos_x, pos_y, speed) -> tuple:
    """Gets the initial position and speed and returns the final position
    """
    
    player_direction = pygame.Vector2(0, 0)
    
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
            player_direction = Vector2(1 / (2 ** 1/2), 1 / (2 ** 1/2))
        
        if player_direction.x == 1 and player_direction.y == -1:
            player_direction = Vector2(1 / (2 ** 1/2), -1 / (2 ** 1/2))
        
        if player_direction.x == -1 and player_direction.y == 1:
            player_direction = Vector2(-1 / (2 ** 1/2), 1 / (2 ** 1/2))
        
        if player_direction.x == -1 and player_direction.y == -1:
            player_direction = Vector2(-1 / (2 ** 1/2), -1 / (2 ** 1/2))
    
    return player_direction.x * speed + pos_x, player_direction.y * speed + pos_y

def move_player_2(pos_x, pos_y, speed) -> tuple:
    """Gets the initial position and speed and returns the final position
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
            player_direction = Vector2(1 / (2 ** 1/2), 1 / (2 ** 1/2))
        
        if player_direction.x == 1 and player_direction.y == -1:
            player_direction = Vector2(1 / (2 ** 1/2), -1 / (2 ** 1/2))
        
        if player_direction.x == -1 and player_direction.y == 1:
            player_direction = Vector2(-1 / (2 ** 1/2), 1 / (2 ** 1/2))
        
        if player_direction.x == -1 and player_direction.y == -1:
            player_direction = Vector2(-1 / (2 ** 1/2), -1 / (2 ** 1/2))
    
    return player_direction.x * speed + pos_x, player_direction.y * speed + pos_y

