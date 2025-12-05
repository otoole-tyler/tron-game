import pygame
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tron Game')
clock = pygame.time.Clock()

Players = []

class Player:
    def __init__(self, color, keybinds):
        self.color = color
        self.keybinds = keybinds # 1:up 2:left 3:down 4:right

        self.x = 0
        self.y = 0

        self.direction_changes = []  # stored as [x, y]
        self.current_direction = 'up'

    def movement(self):
        keys = pygame.key.get_pressed()
        changed_direction = False

        if keys[self.keybinds[0]]:
            if self.current_direction not in ['down', 'up']:
                changed_direction = True
                self.current_direction = 'up'
        elif keys[self.keybinds[1]]:
            if self.current_direction not in ['left', 'right']:
                changed_direction = True
                self.current_direction = 'left'
        elif keys[self.keybinds[2]]:
            if self.current_direction not in ['down', 'up']:
                changed_direction = True
                self.current_direction = 'down'
        elif keys[self.keybinds[3]]:
            if self.current_direction not in ['left', 'right']:
                changed_direction = True
                self.current_direction = 'right'


        if changed_direction: self.direction_changes.append([self.x, self.y]); print(self.current_direction)
            
            

Players.append(Player((255,255,255), [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    for player in Players:
        player.movement()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()