import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 680
        self.WINDOW_HEIGHT = 680
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH ,self.WINDOW_HEIGHT))
        self.boss_menu = BossMenu()
        self.active_boss_level

    def start(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                elif event.type == pygame.MOUSEBOTTONDOWN:
                    self.try_to_click(event, pos)

    def draw(self):
        self.screen.fill(0,0,0)
        self.boss_menu.draw_blocks(self.screen)
        pygame.display.flip()


    def try_to_click(self,pos)
        for block in self.boss_menu.blocks:
            if block.is_clicked(pos):
                if  isinstance(block,LevelChanger)
                self.boss_menu.change_boss_info()







        main = Main()
        main.start()
        pygame.display.flip()