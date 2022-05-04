"""
Projection

Description:
"""
import pygame, sys
import MatrixMultiplication as mm
pygame.init()

window = pygame.display.set_mode([600, 600])
window.fill((0, 0, 0))

points = []
angle = 0

scale = 4

class Vector:
    
    def __init__(self, (x, y, z)):
        
        self.x = x
        self.y = y
        self.z = z

class Vertice:
    
    def __init__(self, corr):
        
        global scale
        
        print(corr[0], corr[1])
        #pygame.draw.circle(window, (255, 255, 255), (corr[0], corr[1]), scale)
        pygame.display.flip()

def win():
    
    while True:
    
        for e in pygame.event.get():
            
            if e.type == pygame.QUIT:
                
                sys.exit()
    
# Square Points
points.append(Vector((50, 150, 0)))
points.append(Vector((150, 50, 0)))
points.append(Vector((150, 150, 0)))
points.append(Vector((50, 50, 0)))

for x in range(0, len(points)):
    
    p = mm.vecMatrix(points[x])
    Vertice(p)
    
angle += 0.01
