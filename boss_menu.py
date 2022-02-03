

    def draw_blocks(self,screen)
        for block in self.blocks:
            block.draw_block(screen)


    def change_boss_info(self,step):
        if step == -1:
            self.change_boss_info_to_the_left()
        else:
            self.change_boss_info_to_the_right()


    def change_boss_info_to_the_right(self):
        if self.blocks[1].level==1:
            return
        self.blocks.pop(-2)
        self.blocks.insert(1,)
    def change_boss_info_to_the_left(self):
        if self.blocks[1].level == 1:
            return
        self.block.pop(-2)
        self.blocks.insert(1,Boss(self.blocks[1].level - 1, 100))
        for i in range(2,5):
            self.blocks[i].block_pos += 100

    def change_boss_info_to_the_right(self):
        self.block.pop(1)
            self.blocks.insert(-1, Boss(self.blocks[-2].level + 1, 400))
        for i in range(1, 4):
            self.blocks[i].block_pos -= 100
