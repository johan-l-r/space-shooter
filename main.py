from typing import Concatenate
import pygame as pg
from os.path import join
import time 
import random

# this needs to be on top
pg.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# game management
running = True

round = 1

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ), pg.SRCALPHA)

# player 
PLAYER_SIZE = 100

player_surface = pg.image.load(join("assets/imgs", "alien.png")).convert_alpha()
player_surface = pg.transform.scale(player_surface, (PLAYER_SIZE, PLAYER_SIZE))
player_rect = player_surface.get_frect(center = (150, WINDOW_HEIGHT / 2))

player_y_pos = (WINDOW_HEIGHT - 150) / 2 # set pos to center of y axis 
player_speed = 5
player_y_direction = 0
player_x_direction = 0


# asteroids 
SPAWN_TIME = 150
ASTEROID_MIN_SIZE = 100

GROWTH_FACTOR = 2
asteroid_max_size = round * ASTEROID_MIN_SIZE * GROWTH_FACTOR
max_asteroids = 15
spawn_timer = 0

asteroids = []

asteroid_surface = pg.image.load(join("assets/imgs", "asteroid.png")).convert_alpha()

def spawn_asteroid():
  global spawn_timer 
  global asteroid_surface

  spawn_timer += 0.1

  if spawn_timer >= SPAWN_TIME and len(asteroids) <= max_asteroids: 
    size = random.uniform(ASTEROID_MIN_SIZE, asteroid_max_size)
    speed = 200 / size

    asteroid_surface = pg.transform.scale(asteroid_surface, (size, size))

    asteroid = pg.FRect(
      WINDOW_WIDTH, 
      random.uniform(0, WINDOW_HEIGHT - size), 
      asteroid_surface.get_frect().width, 
      asteroid_surface.get_frect().height
    )

    asteroids.append((asteroid, asteroid_surface, speed))

    spawn_timer = 0

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
      if event.key == pg.K_a:
        player_x_direction = -1
      if event.key == pg.K_d:
        player_x_direction = 1

    if event.type == pg.KEYUP:
      if event.key == pg.K_w:
        player_y_direction = 0
      if event.key == pg.K_s:
        player_y_direction = 0
      if event.key == pg.K_a:
        player_x_direction = 0
      if event.key == pg.K_d:
        player_x_direction = 0
      
  # UPDATE GAME
  if player_rect.y  < 0: 
    player_rect.y = player_rect.y = 0
  if player_rect.y > WINDOW_HEIGHT - PLAYER_SIZE:
    player_rect.y = WINDOW_HEIGHT - PLAYER_SIZE
  if player_rect.x < 0: 
    player_rect.x = player_rect.x = 0
  if player_rect.x > WINDOW_WIDTH - PLAYER_SIZE:
    player_rect.x = WINDOW_WIDTH - PLAYER_SIZE

  player_rect.y += player_speed * player_y_direction
  player_rect.x += player_speed * player_x_direction


  

  spawn_asteroid()

  # move asteroids
  for rect, _, speed in asteroids: 
    rect.x -= speed

  # teleport asteroids
  for rect, _, speed in asteroids: 
    if rect.x <  -asteroid_max_size: 
      rect.y = random.uniform(0, WINDOW_HEIGHT - rect.height)
      rect.x = WINDOW_WIDTH

  # DRAW GAME
  window.fill((0, 0, 0)) # fill the window with black every frame

  for rect, surface, _ in asteroids: 
    window.blit(surface, rect)

  window.blit(player_surface, player_rect)

  pg.display.update()

pg.quit()
