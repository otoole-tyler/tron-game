import pygame
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tron Game')
clock = pygame.time.Clock()

Players = []

class Player:
    def __init__(self, color, keybinds, x, y, initial_direction, speed=4):
        self.color = color
        self.keybinds = keybinds # 1:up 2:left 3:down 4:right

        self.x = x
        self.y = y

        self.direction_changes = [(self.x, self.y), (self.x, self.y)]  # stored as [x, y]
        self.current_direction = initial_direction
        
        self.speed = speed

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

        if changed_direction: self.direction_changes.append((self.x, self.y))#; # print(self.current_direction)

        if self.current_direction == 'up': self.y -= self.speed
        elif self.current_direction == 'left': self.x -= self.speed
        elif self.current_direction == 'down': self.y += self.speed
        elif self.current_direction == 'right': self.x += self.speed

    def draw(self):
        pygame.draw.lines(screen, self.color, False, self.direction_changes)
        pygame.draw.line(screen, self.color, self.direction_changes[-1], (self.x, self.y))

    def is_on_line(self, start, end):
        x1, y1 = start
        x2, y2 = end
        if x1 == x2:  # vertical
            return self.x == x1 and min(y1, y2) <= self.y <= max(y1, y2)
        elif y1 == y2:  # horizontal
            return self.y == y1 and min(x1, x2) <= self.x <= max(x1, x2)
        return False
            
            

Players.append(Player((255, 0, 0), [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d], 750, 400, 'left'))
Players.append(Player((0, 0, 255), [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT], 50, 400, 'right'))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    for player in Players:
        player.movement()
        player.draw()
        for other_player in Players:
            points = other_player.direction_changes + [(other_player.x, other_player.y)]
            for i in range(len(points)-1 - (other_player == player)):
                if player.is_on_line(points[i], points[i+1]):
                    exit()


    pygame.display.flip()
    clock.tick(60)
pygame.quit()