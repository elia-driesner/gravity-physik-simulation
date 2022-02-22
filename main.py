import math
import pygame
import os

pygame.init()
os.system('clear')

wn_size = [1400, 700]
wn = pygame.display.set_mode(wn_size)
pygame.display.set_caption('gravity physic simulation')

clock = pygame.time.Clock()
FPS = 60

run = True

pixel_meter = 10

objects = []

class Object:
    def __init__(self, x, y, height, width, mass, color):
        self.mass = mass      
        self.width = width
        self.height = height      
        self.x, self.y = x, y
        self.color = color
        
        self.start_x = x
        self.start_y = y
        
        
def calc_gravity(m1, m2, r, o1, o2):
    F = ((6.67428 * 10e-11) * m1 * m2) / (r * r)
    a = F / m2
    t = 0.0166666667
    s = (F / m2) * t * t
    
    o1_x = o1.x + (o1.width / 2)
    o2_x = o2.x + (o2.width / 2)
    
    # if o2_x < o1_x:
    #     o2.x += (o2.start_x + s) * pixel_meter
    # else: 
    #     o2.x += (o2.start_x + s) * pixel_meter
    
    if o2_x < o1_x:
        o2.x += (s) * pixel_meter
    else: 
        o2.x += (s) * pixel_meter
        
    print(s)
        
    
# calc_gravity(m1 = 5.972 * 10e24 , m2 = 60, r =  6.38 * 10e6)

objects.append(Object(900, 100, 100, 100, 10000000000000000000, (0, 0, 255)))

objects.append(Object(0, 250, 100, 100, 1, (0, 255, 0)))

while run:  
    clock.tick(FPS)
    
    wn.fill((0, 0, 0))
    for element in objects:
        if element != objects[0]:
            pygame.draw.rect(wn, element.color, [element.x, element.y, element.width, element.height], 0)
        else:
            pygame.draw.circle(wn, element.color, (element.x, wn_size[1] / 2 - element.height / 2), element.width / 2)
    pygame.display.update()
    
    calc_gravity(m1 = objects[0].mass , m2 = objects[1].mass, r =  pixel_meter * (objects[0].x - objects[1].x), o1 = objects[0], o2 = objects[1])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
    