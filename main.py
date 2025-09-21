from os import posix_fallocate
import pygame as pg
from pygame.display import get_surface

# this needs to be on top
pg.init()

# CONSTANTS
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

running = True

# window
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ))

# player 
player = pg.image.load("./assets/imgs/alien.png").convert_alpha()
player = pg.transform.scale(player, (150, 150))

player_y_pos = (WINDOW_HEIGHT - 150) / 2 # set pos to center of y axis 
player_speed = 5
player_y_direction = 0

# game loop 
while running: 
  for event in pg.event.get(): # get "unlistened" events
    if event.type == pg.QUIT: # end game when window closed
      running = False

    if event.type == pg.KEYDOWN:
      if event.key == pg.K_w:
        player_y_direction = -1
      if event.key == pg.K_s:
        player_y_direction = 1

    if event.type == pg.KEYUP:
      if event.key == pg.K_w:
        player_y_direction = 0
      if event.key == pg.K_s:
        player_y_direction = 0
      
  # UPDATE GAME
  player_y_pos += player_speed * player_y_direction

  # DRAW GAME
  window.fill((0, 0, 0)) # fill the window with black every frame

  window.blit(player, (50, player_y_pos))

  pg.display.update()

pg.quit()
