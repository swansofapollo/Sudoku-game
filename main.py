import pygame
from generator import Generator
NUMS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
        'd': 13, 'e': 14, 'f': 15}
NOT_NUMS = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
            13: 'D', 14: 'E', 15: 'F'}


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.gen = Generator(n=4, difficulty = 80)
        # self.table = [[''] * self.width for _ in range(self.height)]
        self.table = self.gen.generate_field()
        for el in range(len(self.table)):
            for i in range (len(self.table[el])):
                if self.table[el][i] == -1:
                    self.table[el][i] = ''
                else:
                    self.table[el][i] = NOT_NUMS[self.table[el][i]]
        self.editable = [[True if self.table[i][j] == '' else False for j in range(self.width)] for i in range(self.height)]
        self.coord = (0, 0)
        self.cell_size = 40
        self.left = 10
        self.top = 10
        self.notes = [[[False] * 16] * self.width for _ in range(self.height)]
        self.diapason = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        self.edit_notes = False

    def set_view(self, cell_size, left, top):
        self.cell_size = cell_size
        self.left = left
        self.top = top

    def render(self, screen):
        for i in range(self.height // 4):
            for j in range(self.width // 4):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, pygame.Color('#989898'), (
                        self.left + self.cell_size * j * 4, self.top + self.cell_size * i * 4, self.cell_size * 4,
                        self.cell_size * 4),
                                     0)
                else:
                    pygame.draw.rect(screen, pygame.Color('#535353'), (
                        self.left + self.cell_size * j * 4, self.top + self.cell_size * i * 4, self.cell_size * 4,
                        self.cell_size * 4),
                                     0)
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color('black'), (
                    self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size,
                    self.cell_size),
                                 1)

        font = pygame.font.Font(None, 68)

        for i in range(16):
            text = font.render(NOT_NUMS[i], True, (255, 255, 255))
            screen.blit(text, (17+40*i, 700))

        fonttt = pygame.font.Font(None, 30)


        if self.edit_notes:
            pygame.draw.rect(screen, (60, 170, 60), (self.left, self.top+self.cell_size*16+10, self.cell_size*16, 30), 0)
            text = fonttt.render('note mode [SPACE]', True, (0,140,240))

        else:
            pygame.draw.rect(screen, (218, 112, 214),
                             (self.left, self.top + self.cell_size * 16 + 10, self.cell_size * 16, 30), 0)
            text = fonttt.render('normal mode [SPACE]', True, (0, 140, 240))
        screen.blit(text, (220, self.top+self.cell_size*16+15))



        font = pygame.font.Font(None, 55)
        pygame.draw.rect(screen, pygame.Color('white'), (
            self.left+2 + self.cell_size * self.coord[0], self.top +2+ self.cell_size * self.coord[1], self.cell_size-4,
            self.cell_size-4),
                         0)



        for i in range(self.height):
            for j in range(self.width):

                text = font.render(self.table[j][i], True, (245,254,9) if self.editable[j][i] else (0,0,0))
                text_x = self.left + self.cell_size * j + 10
                text_y = self.top + self.cell_size * i + 3
                # text_rect = text.get_rect(center=(text_x +self.cell_size/2, text_y+self.cell_size/2 ))
                screen.blit(text, (text_x,text_y))
        font_1 = pygame.font.Font(None, 20)

        for i in range(self.height):
            for j in range(self.width):
                for z in range(16):
                    if self.notes[j][i][z] == True and self.table[j][i] == '':
                        text = font_1.render(NOT_NUMS[z], True, (0, 0, 0))
                        note_x = self.left + self.cell_size * j + 10
                        note_y = self.top + self.cell_size * i + 3
                        screen.blit(text, (note_x, note_y))

    def get_cell(self, mous_coord):
        x, y = mous_coord
        x -= self.left
        y -= self.top
        if x < 0 or y < 0 or x > self.width * self.cell_size or y > self.height * self.cell_size :
            return None
        return x // self.cell_size, y // self.cell_size

    def get_button(self, mouse_coord):
        x, y = mouse_coord
        x -= self.left
        y -= self.top
        if x < 0 or y < 690 or x > self.width * self.cell_size or y > 725:
            return None
        if self.coord is not None:
            self.table[self.coord[0]][self.coord[1]] = NOT_NUMS[x // self.cell_size]



    def on_click(self, cell_coords):
        self.coord = cell_coords


    def on_key_down(self, key):
        if self.editable[self.coord[0]][self.coord[1]]:

            if chr(key) == ' ':
                self.edit_notes = not self.edit_notes
            if chr(key) in self.diapason:
                if self.edit_notes and chr(key) != ' ':
                    self.notes[self.coord[0]][self.coord[1]][NUMS[chr(key)]] = True
                else:
                    self.table[self.coord[0]][self.coord[1]] = chr(key).upper() if chr(key).isalpha() else chr(key)

    def get_click(self, mouse_pos):
        self.get_button(mouse_pos)
        cell_coords = self.get_cell(mouse_pos)
        if cell_coords is None:
            return
        self.on_click(cell_coords)



if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    pygame.display.set_caption('___')
    screen = pygame.display.set_mode(size)
    table = Board(16, 16)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                table.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                table.on_key_down(event.key)

        screen.fill((30, 30, 30))
        table.render(screen)

        pygame.display.flip()
    pygame.quit()
