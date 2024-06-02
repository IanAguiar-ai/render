"""
Render with the following features:

- Only polygons;
- Light;
- Reflexes;
- Textures;
"""

from operations import vector, center_polygon, vectorial_product, find_normal_vector, transpose_on_screen, light_in_polygon, distance_two_points
import pygame
from time import sleep
from random import random

class Screen:
    """
    Screen and its properties
    """
    __slots__ = ("position", "x_lim", "y_lim", "width", "height")
    def __init__(self, center:(float, float, float), x:int, y:int):
        self.position:(float, float, float) = center
        self.x_lim:(float, float) = (center[0] - int(x/2), center[0] + int(x/2))
        self.y_lim:(float, float) = (center[1] - int(y/2), center[1] + int(y/2))
        self.width:int = x
        self.height:int = y

class Light:
    """
    Light with basic properties
    """
    __slots__ = ("position", "color", "intensity", "ambient")
    def __init__(self, position:(float, float, float), color:(int, int, int), intensity:float = 10, ambient:float = 0.1):
        self.position:(int, int, int) = position
        self.color:(int, int, int) = color
        self.intensity:float = intensity
        self.ambient:float = ambient #ambient light [0, 1]

class Polygon:
    """
    Polygon, simpler 3D shape
    """
    __slots__ = ("p1", "p2", "p3", "p1_p2", "p2_p3", "p1_p3", "position", "color", "normal_vector", "positions_screen", "screen", "reflection")
    def __init__(self, p1:(float, float, float), p2:(float, float, float), p3:(float, float, float), screen:Screen, color:(int, int, int) = (10, 10, 250), reflection:float = 0.2):
        self.p1:(float, float, float) = p1 #Point in space
        self.p2:(float, float, float) = p2 #Point in space
        self.p3:(float, float, float) = p3 #Point in space
        self.p1_p2:(float, float, float) = vector(p1, p2) #Vector
        self.p2_p3:(float, float, float) = vector(p2, p3) #Vector
        self.p1_p3:(float, float, float) = vector(p1, p3) #Vector
        self.position:(float, float, float) = center_polygon(self) #Center point of the polygon
        self.color:(int, int, int) = color #(int(random()*255), int(random()*255), int(random()*255))
        self.normal_vector:(float, float, float) = find_normal_vector(self) #Vector
        self.positions_screen:((float, float), (float, float), (float, float)) = transpose_on_screen(self, screen)
        self.screen:Screen = screen
        self.reflection:float = reflection #[0, 1]

    def add_composition(self, light:Light):
        self.color:(int, int, int) = light_in_polygon(self, light, self.screen)
        #print(f"Color: {self.color}\n\n")

def multyple_polygons(polygon:Polygon) -> list:
    """
    Multyple the number of polygons
    """
##    return [Polygon(polygon.p1, polygon.p2, polygon.position, screen = polygon.screen, color = polygon.color),
##            Polygon(polygon.p1, polygon.position, polygon.p3, screen = polygon.screen, color = polygon.color),
##            Polygon(polygon.position, polygon.p2, polygon.p3, screen = polygon.screen, color = polygon.color)]
    def mean(a:list, b:list) -> list:
        return [(a[i]+b[i])/2 for i in range(3)]

    p1_p2 = mean(polygon.p1, polygon.p2)
    p2_p3 = mean(polygon.p2, polygon.p3)
    p1_p3 = mean(polygon.p1, polygon.p3)
    p1 = polygon.p1
    p2 = polygon.p2
    p3 = polygon.p3

    return [Polygon(p1,     p1_p2,      p1_p3, screen = polygon.screen, color = polygon.color, reflection = polygon.reflection),
            Polygon(p1_p2,  p2,         p2_p3, screen = polygon.screen, color = polygon.color, reflection = polygon.reflection),
            Polygon(p1_p2,  p2_p3,      p3, screen = polygon.screen, color = polygon.color, reflection = polygon.reflection),
            Polygon(p1_p3,  p1_p2,       p3, screen = polygon.screen, color = polygon.color, reflection = polygon.reflection)]

def multyple_fast(list_polygons:list, times:int = 1) -> list:
    """
    Multyple polygons fast
    """
    times -= 1
    polygons_temp:list = [multyple_polygons(polygon) for polygon in list_polygons]
    polygons:list = []
    for polygon in polygons_temp:
        polygons.extend(polygon)

    if times <= 0:
        return polygons
    else:
        return multyple_fast(polygons, times)

def reorganize(polygons:list, screen:Screen) -> list:
    """
    #Reorganize the polygons
    """
    distances:list = []
    for polygon in polygons:
        #print(distance_two_points(polygon, screen))
        distances.append([polygon, distance_two_points(polygon, screen)])
    distances:list = sorted(distances, key = lambda x:x[1], reverse = True)
    polygons:list = []
    for d in distances:
        polygons.append(d[0])
    polygons.sort(key = lambda poly: poly.position[2], reverse = True)
    return polygons

def render(screen:Screen, polygons:list, light:list, steps:bool = True) -> None:
    """
    Set up the scene given the polygons and lights
    """
    global width, height
    pygame.init()
    
    pygm = pygame.display.set_mode((screen.width, screen.height))
    pygame.display.set_caption("RENDER")

    polygons = reorganize(polygons, screen)
    if type(steps) == float or type(steps) == int:
        t:float = steps
        steps:bool = True
    else:
        t:float = 0.5/len(polygons)
    for p in polygons:
        pygame.draw.polygon(pygm, p.color, p.positions_screen)
        if steps:
            pygame.display.flip()
            sleep(t)
        for l in light:
            p.add_composition(l)
            if steps:
                sleep(t)
        pygame.draw.polygon(pygm, p.color, p.positions_screen)
        if steps:
            pygame.display.flip()
            sleep(t)
    pygame.display.flip()
