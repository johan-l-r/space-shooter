import pygame as pg

# this needs to be on top
pg.init()

# CONSTANTS
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

running = True

# window
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ))

# game loop 
while running: 
  for event in pg.event.get(): # get "unlistened" events
    if event.type == pg.QUIT: # end game when window closed
      running = False
  # UPDATE GAME

  # DRAW GAME
  window.fill((0, 0, 0)) # fill the window with black every frame

pg.quit()
