# Definir la cuadrícula de palabras y sus pistas
grid = [
    ['P', 'Y', 'T', 'H', 'O', 'N'],
    ['R', 'E', 'C', 'T', 'A', 'N', 'G', 'L', 'E'],
    ['L', 'I', 'S', 'T'],
    ['C', 'R', 'O', 'S', 'S', 'W', 'O', 'R', 'D'],
    ['H','O','L','A']
    # ... (añade más palabras según sea necesario)
]

# Pistas correspondientes a las palabras en la cuadrícula
clues = {
    'PYTHON': 'Lenguaje de programación',
    'RECTANGLE': 'Figura geométrica con cuatro ángulos rectos',
    'LIST': 'Estructura de datos en Python',
    'CROSSWORD': 'Este juego de palabras'
    # ...
}



import pygame
import sys

# Tamaño de la ventana y de cada celda en la cuadrícula
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CELL_SIZE = 40

def draw_grid(screen):
    # Dibuja la cuadrícula
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, (255, 255, 255), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            font = pygame.font.SysFont(None, 24)
            text = font.render(cell, True, (255, 255, 255))
            screen.blit(text, (x * CELL_SIZE + 15, y * CELL_SIZE + 15))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Crucigrama')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Relleno de fondo negro
        draw_grid(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()


