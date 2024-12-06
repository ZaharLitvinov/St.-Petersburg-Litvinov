import sys
import pygame

def m():
    pygame.init()
    screen = pygame.display.set_mode((300, 400))
    coordinates = (0, 0)
    radius = 0
    color = "yellow"
    flag = False
    running = True
    p_l =pygame.USEREVENT + 25
    pygame.time.set_timer(p_l, 10)
    while running:
        for event in pygame.event.get():            
            if event.type == pygame.MOUSEBUTTONUP:
                radius = 0
                coordinates = event.pos
                flag = True
                screen.fill(pygame.Color("blue"))
            if event.type == pygame.QUIT:
                running = False
            if event.type == p_l and flag:
                radius += 1
                pygame.draw.circle(screen, pygame.Color(color), coordinates, radius)
        pygame.display.flip()
        pygame.time.Clock().tick(50)
    pygame.quit()



sys.exit(m())
