from os import posix_fallocate
import pygame as pg

# this needs to be on top
pg.init()

# CONSTANTS
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

running = True

# window
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ))
player = pg.image.load("./assets/imgs/alien.png")
player = pg.transform.scale(player, (150, 150))

# game loop 
while running: 
  for event in pg.event.get(): # get "unlistened" events
    if event.type == pg.QUIT: # end game when window closed
      running = False
  # UPDATE GAME

  # DRAW GAME
  window.fill((0, 0, 0)) # fill the window with black every frame
  window.blit(player, (50, 50))
  pg.display.update()

pg.quit()
