# -*- coding: UTF-8 -*-

from pygame.locals import *
import pyscroll
from pytmx.util_pygame import load_pygame

from constants import BLACK, GAME_WIDTH
from helpers import get_map_filename, get_max_soldiers, load_image
from sprite import Sprite
from text import create_prompt


class Beginning(object):
    def __init__(self, game, screen):
        self.game = game
        map_filename = get_map_filename('beginning.tmx')
        self.screen = screen
        self.tmx_data = load_pygame(map_filename)
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 1
        self.group = pyscroll.group.PyscrollGroup(map_layer=self.map_layer)
        mid = self.tmx_data.width/2
        speed = 1.5
        self.moroni = Sprite(self.tmx_data, self.game, 'moroni', [mid,1], speed=speed, direction='s', walking=True)
        self.group.add(self.moroni)
        self.teancum = Sprite(self.tmx_data, self.game, 'teancum', [1,mid], speed=speed, direction='e', walking=True)
        self.group.add(self.teancum)
        self.amalickiah = Sprite(self.tmx_data, self.game, 'amalickiah', [mid*2-1,mid], speed=speed, direction='w', walking=True)
        self.group.add(self.amalickiah)
        self.paces_left = 6
        self.pledge_image = load_image('pledge.png')
        self.prompt = create_prompt(
            'So long as our enemies threaten our liberty and our families, we covenant before God to defend them. '
            'May we stand side by side as fellow protectors of this land until the day we die.'
        )

    def draw(self):
        if self.paces_left > 0:
            self.group.draw(self.screen)
        else:
            self.screen.fill(BLACK)
            self.screen.blit(self.pledge_image, ((GAME_WIDTH - self.pledge_image.get_width())/2, 32))
            self.screen.blit(self.prompt.surface, ((GAME_WIDTH - self.prompt.width)/2, 160))

    def update(self, dt):
        if self.paces_left > 0:
            moved = False
            for sprite in [self.moroni, self.teancum, self.amalickiah]:
                m = sprite.move(sprite.direction)
                if sprite == self.moroni:
                    moved = m
            if moved:
                self.paces_left -= 1
            self.group.update(dt)
        else:
            self.prompt.update(dt)

    def handle_input(self, pressed):
        if self.paces_left == 0:
            self.prompt.handle_input(pressed)
            if pressed[K_x] and not self.prompt.has_more_stuff_to_show():
                self.game.set_screen_state('game')
                self.game.update_game_state({
                    'company': [
                        {
                            'name': 'moroni',
                            'soldiers': get_max_soldiers('moroni', 1),
                            'items': [{'name': 'knife', 'equipped': True}, {'name': 'robe', 'equipped': True}],
                        },
                        {
                            'name': 'teancum',
                            'soldiers': get_max_soldiers('teancum', 1),
                            'items': [{'name': 'knife', 'equipped': True}, {'name': 'robe', 'equipped': True}],
                        },
                        {
                            'name': 'amalickiah',
                            'soldiers': get_max_soldiers('amalickiah', 1),
                            'items': [{'name': 'knife', 'equipped': True}, {'name': 'robe', 'equipped': True}],
                        },
                    ],
                    'level': 1,
                    'acquired_items': [],
                    'surplus': [],
                })
                dialog = create_prompt(
                    'An epistle arrived while you were away. The chief judge is summoning you in the palace at Zarahemla. '
                    'You can find the city of Zarahemla to the west.'
                )
                self.game.set_current_map('house_of_moroni', [13,12], 'n', followers='trail', dialog=dialog)
                self.prompt.shutdown()
