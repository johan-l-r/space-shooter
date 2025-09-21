# space-shooter
Oh no! Mr. Alien is in trouble! His spaceship is surrounded by incoming asteroids, and if he doesn’t blast them away, it’s game over. 
This is my very first project made with the Pygame framework. I’m using this repository to not only share the game, but also document what I learn along the way. Hopefully, this will help beginners understand how to start with Pygame and build their own cool games.

## Getting started 
### Prerequisites
- Python 3.9+
- Pygame

### Install Pygame with:
```bash
pip install pygame
```

### Running the Game
Clone the repo and run the main script:
```bash
git clone https://github.com/johan-l-r/space-shooter.git
cd space-shooter
python main.py
```

## Learning notes
While making this game, I’m documenting the Pygame basics I encounter:

### Creating a window
The first to make a game is having a window where to put your amazing visuals. So, to do that we 
need to: 
1. Import `pygame` (remember to source your virtual environment first)
2. Initialize `pygame`s modules with `pygame.init()`
3. Create a display **surface** (the main screen)

```python
import pygame as pg

pg.init()

# create the main window
window = pg.display.set_mode((1280, 720))
```

### Surfaces 
In Pygame, surfaces are like canvases. You can draw shapes, text, or images onto them, then “blit” (copy) them onto the main window. Every image you see in a Pygame project is just a surface under the hood.
