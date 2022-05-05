"""
Projection

Description:
"""
import pygame, sys
import MatrixMultiplication as mm
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
window.fill((0, 0, 0))

points = []
angle = 0

scale = 4

# Functions and Matrices
projection = [
    [1, 0, 0],
    [0, 1, 0]
]

class Vector:
    
    def __init__(self, (x, y, z)):
        
        self.x = x
        self.y = y
        self.z = z

class Vertice:
    
    def __init__(self, corr):
        
        global scale
        
        x = corr[0][0]
        y = corr[1][0]
        
        x += (SCREEN_WIDTH / 2)
        y -= (SCREEN_HEIGHT / 2) * -1
        
        pygame.draw.circle(window, (255, 255, 255), (x, y), scale)
        pygame.display.flip()

def win():
    
    while True:
    
        for e in pygame.event.get():
            
            if e.type == pygame.QUIT:
                
                sys.exit()
    
# Square Points
points.append(Vector((-50, -50, 0)))
points.append(Vector((50, -50, 0)))
points.append(Vector((50, 50, 100)))
points.append(Vector((-50, 50, 100)))

for x in range(0, len(points)):
    
    p = mm.vecMatrix(points[x])
    Vertice(p)
    
angle += 0.01
