from typing import Concatenate
import pygame as pg
from os.path import join
from random import randint

# this needs to be on top
pg.init()

# CONSTANTS
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

running = True

# window
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ), pg.SRCALPHA)

# player 
PLAYER_SIZE = 150

player_surface = pg.image.load(join("assets/imgs", "alien.png")).convert_alpha()
player_surface = pg.transform.scale(player_surface, (PLAYER_SIZE, PLAYER_SIZE))
player_rect = player_surface.get_frect(center = (100, WINDOW_HEIGHT / 2))

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
  player_rect.y += player_speed * player_y_direction

  if player_rect.y  < 0: 
    player_rect.y = player_rect.y = 0
  if player_rect.y > WINDOW_HEIGHT - PLAYER_SIZE:
    player_rect.y = WINDOW_HEIGHT - PLAYER_SIZE

  # DRAW GAME
  window.fill((0, 0, 0)) # fill the window with black every frame

  window.blit(player_surface, player_rect)

  pg.display.update()

pg.quit()
