import pygame
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Caption')
clock = pygame.time.Clock()

class Player:
    def __init__(self, color, keybinds):
        self.color = color
        self.keybinds = keybinds

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    # im a comment

    pygame.display.flip()
    clock.tick(60)
pygame.quit()