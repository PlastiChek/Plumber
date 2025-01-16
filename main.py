import pygame


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.mouse_pos = None

    def set_view(self, left: int, top: int, cell_size: int):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screem: pygame.Surface):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screem, self.black,
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size,
                                  self.cell_size))
                pygame.draw.rect(screem, self.white,
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size,
                                  self.cell_size), 1)

    def get_click(self, mouse_pos: tuple[float, float]) -> None:
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos: tuple[float, float]) -> tuple[int, int]:
        x, y = mouse_pos
        self.mouse_pos = ((x - 10) // 30, (y - 10) // 30)
        if (x > 160 or x < 10) or (y > 220 or y < 10):
            self.mouse_pos = None

    def on_click(self, cell: tuple[int, int]):
        print(self.mouse_pos)


pygame.init()
board = Board(5, 7)
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Трубопроводчик')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()

pygame.quit()
