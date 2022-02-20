import math
import pygame
import os

pygame.init()
os.system('clear')

wn_size = [700, 700]
wn = pygame.display.set_mode(wn_size)
pygame.display.set_caption('gravity physic simulation')

clock = pygame.time.Clock()
FPS = 60

run = True

objects = []

class Object:
    def __init__(self, x, y, height, width, mass, color):
        self.mass = mass      
        self.width = width
        self.height = height      
        self.x, self.y = x, y
        self.color = color
        
        
def calc_gravity(m1, m2, r):
    F = ((6.67428 * 10e-11) * m1 * m2) / (r * r) # Calculate Gravity and Output Fg = N
    print(f'{F} Newton')
    
def update_physics(objects):
    pass
    
# calc_gravity(m1 = 5.972 * 10e24 , m2 = 60, r =  6.38 * 10e6)

objects.append(Object(100, 100, 100, 100, 10, (255, 0, 0)))
objects.append(Object(300, 100, 100, 100, 20, (0, 255, 0)))

while run:  
    clock.tick(FPS)
    
    wn.fill((0, 0, 0))
    for element in objects:
        pygame.draw.rect(wn, element.color, [element.x, element.y, element.width, element.height], 0)
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
    