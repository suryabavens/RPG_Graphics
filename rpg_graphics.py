import pygame

# initializing game engine
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (197, 210, 12)
RED = (251, 33, 5)
BlUE = (14, 206, 231)
font = pygame.font.SysFont('Calibri', 25, True, False)
text1 = font.render("KITCHEN", True, BLACK)
text2 = font.render("HALL", True, BLACK)
text3 = font.render("DININGROOM", True, BLACK)
pi = 3.141592653
move = ' '
# setting up the window
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption(" RPG_GAME")

done = False

inventory = []
rooms1 = {'kitchen': {'north': 'hall', 'pan': 'item1'},
          'hall': {'south': 'kitchen', 'chair': 'item1', 'east': 'diningroom'}, 'diningroom': {'west': 'hall'}}
currentRoom = 'hall'
pos = [100, 100, 30, 30]


def movement_fun():
    global currentRoom

    if move in rooms1[currentRoom]:
        currentRoom = rooms1[currentRoom][move]
        if currentRoom is 'kitchen':
            pos[0] = 100
            pos[1] = 310
        elif currentRoom is 'hall':
            pos[0] = 100
            pos[1] = 100
        elif currentRoom is 'diningroom':
            pos[0] = 300
            pos[1] = 100


clock = pygame.time.Clock()

# Program Loop

while not done:
    # event_loop
    # screen.fill(WHITE)

    # pygame.draw.rect(screen,BLACK,[10,10,50,50])
    # pygame.draw.rect(screen,BLACK,[60,60,50,50])
    for event in pygame.event.get():
        if pygame.event.EventType == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                done = True
            if event.key == pygame.K_w:
                move = 'north'
                movement_fun()
            if event.key == pygame.K_s:
                move = 'south'
                movement_fun()
            if event.key == pygame.K_a:
                move = 'west'
                movement_fun()
            if event.key == pygame.K_d:
                move = 'east'
                movement_fun()

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (10, 10), (10, 410), 5)
    pygame.draw.line(screen, BLACK, (10, 10), (410, 10), 5)
    pygame.draw.line(screen, BLACK, (410, 10), (410, 210), 5)
    pygame.draw.line(screen, BLACK, (410, 210), (135, 210), 5)
    pygame.draw.line(screen, BLACK, (210, 135), (210, 410), 5)
    pygame.draw.line(screen, BLACK, (10, 410), (210, 410), 5)
    pygame.draw.line(screen, BLACK, (10, 210), (85, 210), 5)
    pygame.draw.line(screen, BLACK, (210, 10), (210, 85), 5)
    screen.blit(text1, [65, 380])
    screen.blit(text2, [85, 15])
    screen.blit(text3, [235, 15])
    pygame.draw.rect(screen, RED, pos)
    pygame.display.flip()
    clock.tick(60)
