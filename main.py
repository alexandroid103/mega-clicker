import pygame
class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 680
        self.WINDOW_HEIGHT = 680
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH ,self.WINDOW_HEIGHT))



    def start(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
    def draw(self):
        self.bosmenu.draw_blocks(self.screen)
main = Main()
main.start()
pygame.display.flip()