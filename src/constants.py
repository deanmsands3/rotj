# -*- coding: UTF-8 -*-

from pygame.locals import *

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
COPPER = (164, 82, 41)

# sizes
TILE_SIZE = 16 # pixels
GAME_WIDTH = 256 # pixels (before scaling)
GAME_HEIGHT = 240 # pixels (before scaling)

ITEMS = {
    'knife': {
        'attack_points': 10,
    },
    'robe': {
        'armor_class': 10,
    },
}

# we may or may not reference these
EVENT_NAMES = {
    QUIT: 'QUIT',
    ACTIVEEVENT: 'ACTIVEEVENT',
    KEYDOWN: 'KEYDOWN',
    KEYUP: 'KEYUP',
    MOUSEMOTION: 'MOUSEMOTION',
    MOUSEBUTTONDOWN: 'MOUSEBUTTONDOWN',
    MOUSEBUTTONUP: 'MOUSEBUTTONUP',
    JOYAXISMOTION: 'JOYAXISMOTION',
    JOYBALLMOTION: 'JOYBALLMOTION',
    JOYHATMOTION: 'JOYHATMOTION',
    JOYBUTTONDOWN: 'JOYBUTTONDOWN',
    JOYBUTTONUP: 'JOYBUTTONUP',
    VIDEORESIZE: 'VIDEORESIZE',
    VIDEOEXPOSE: 'VIDEOEXPOSE',
}
