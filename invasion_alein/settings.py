import pygame

class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = pygame.image.load('images/fondo.png')

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.ship_speed = 2

        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allow = 3
        self.alien_speed = 0.7
        self.fleet_drop_speed = 7
        self.flett_direccion = 0.5
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 2
        self.bullet_speed = 3.0
        self.alien_speed = 0.8
        self.flett_direccion = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.aliens_points = int(self.alien_points * self.score_scale)





