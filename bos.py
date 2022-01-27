import pygame


class Boss:
    def __init__(self, level, false=None):
        self.health =level*100
        self.golda = level
        self.level = level-1*1.5

        self.font = pygame.font.SysFont("arial",30)
        self.block_picture = self.font.render(str(level),false, (0,0,225))
        self.block.pos=(block_pos + 30, 30)
        self.picture = pygame.image.load('img//boss.png')
        self.pos = (100,100)

    def draw_block(self,screen):
        screen.blit(self.block_picture,self.block_pos)

