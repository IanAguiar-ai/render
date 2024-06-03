"""
Render with the following features:

- Only polygons;
- Light;
- Reflexes;
- Textures;
"""

from operations import vector, normalized, center_polygon, vectorial_product, find_normal_vector, transpose_on_screen, transpose_light_on_screen, light_in_polygon, distance_two_points, distance_two_points_vector
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
    __slots__ = ("position", "color", "intensity", "ambient", "size", "positions_screen")
    def __init__(self, position:[float, float, float], color:[int, int, int], screen:Screen, intensity:float = 10, ambient:float = 0.1, size:int = 5):
        self.position:[int, int, int] = position
        self.color:[int, int, int] = color
        self.intensity:float = intensity
        self.ambient:float = ambient #ambient light [0, 1]
        self.positions_screen:(float, float) = transpose_light_on_screen(self, screen)
        self.size:float = 1/size

class Polygon:
    """
    Polygon, simpler 3D shape
    """
    __slots__ = ("p1", "p2", "p3", "p1_p2", "p2_p3", "p1_p3", "position", "color", "color_to_plot", "normal_vector", "positions_screen", "screen", "reflection", "see", "metalic", "rough", "dispersion_light", "parameters", "texture")
    def __init__(self, p1:(float, float, float), p2:(float, float, float), p3:(float, float, float), screen:Screen, color:(int, int, int) = (10, 10, 250), reflection:float = 0.2, metalic:float = 0.3, rough:float = 0.7, dispersion_light:float = 2, texture:"function" = False):
        self.p1:(float, float, float) = p1 #Point in space
        self.p2:(float, float, float) = p2 #Point in space
        self.p3:(float, float, float) = p3 #Point in space
        self.p1_p2:(float, float, float) = vector(p1, p2) #Vector
        self.p2_p3:(float, float, float) = vector(p2, p3) #Vector
        self.p1_p3:(float, float, float) = vector(p1, p3) #Vector
        self.position:(float, float, float) = center_polygon(self) #Center point of the polygon
        if color == None:
            self.color:(int, int, int) = (int(random()*255), int(random()*255), int(random()*255))
        else:
            self.color:(int, int, int) = color
        self.color_to_plot:(int, int, int) = self.color
        self.normal_vector:(float, float, float) = find_normal_vector(self) #Vector
        self.positions_screen:((float, float), (float, float), (float, float)) = transpose_on_screen(self, screen)
        self.screen:Screen = screen
        self.reflection:float = reflection #[0, 1]
        self.see:bool = True#self.see_in_screen()
        self.metalic:float = metalic
        self.rough:float = rough
        self.dispersion_light:float = 1/dispersion_light
        self.texture:"function" = texture
        self.parameters:dict = {"color":color,
                                "reflection":reflection,
                                "metalic":metalic,
                                "rough":rough,
                                "dispersion_light":dispersion_light,
                                "texture":texture}

    def add_composition(self, light:Light):
        """
        Compositions to polygon
        """
        self.color_to_plot:(int, int, int) = light_in_polygon(self, light, self.screen)
        #print(f"Color: {self.color}\n\n")

    def see_in_screen(self):
        """
        If the camera sees the polygon
        """
        camera_vector:(float, float, float) = normalized(vector(self.position, self.screen.position))
        exposition:float = camera_vector[0] * self.normal_vector[0] + \
                           camera_vector[1] * self.normal_vector[1] + \
                           camera_vector[2] * self.normal_vector[2]
        if exposition > -.72:
            return True
        else:
            return False

def multyple_polygons(polygon:Polygon, mode:int = 2) -> list:
    """
    Multyple the number of polygons
    """
    if mode == 0:
        return [Polygon(polygon.p1, polygon.p2, polygon.position, screen = polygon.screen, color = polygon.color),
                Polygon(polygon.p1, polygon.position, polygon.p3, screen = polygon.screen, color = polygon.color),
                Polygon(polygon.position, polygon.p2, polygon.p3, screen = polygon.screen, color = polygon.color)]
    
    def mean(a:list, b:list) -> list:
        return [(a[i]+b[i])/2 for i in range(3)]

    p1_p2 = mean(polygon.p1, polygon.p2)
    p2_p3 = mean(polygon.p2, polygon.p3)
    p1_p3 = mean(polygon.p1, polygon.p3)
    p1 = polygon.p1
    p2 = polygon.p2
    p3 = polygon.p3

    if mode == 1:
        return [Polygon(p1,     p1_p2,      p1_p3,  screen = polygon.screen, **polygon.parameters),
                Polygon(p1_p2,  p2,         p2_p3,  screen = polygon.screen, **polygon.parameters),
                Polygon(p1_p2,  p2_p3,      p3,     screen = polygon.screen, **polygon.parameters),
                Polygon(p1_p3,  p1_p2,      p3,     screen = polygon.screen, **polygon.parameters)]

    if mode == 2:
        d1 = distance_two_points_vector(p1, p2)
        d2 = distance_two_points_vector(p2, p3)
        d3 = distance_two_points_vector(p1, p3)

        if d1 >= d2 and d1 >= d3:
            return [Polygon(p1_p2, p2, p3, screen=polygon.screen, **polygon.parameters),
                    Polygon(p1, p1_p2, p3, screen=polygon.screen, **polygon.parameters)]
        elif d2 >= d1 and d2 >= d3:
            return [Polygon(p1, p2, p2_p3, screen=polygon.screen, **polygon.parameters),
                    Polygon(p1, p2_p3, p3, screen=polygon.screen, **polygon.parameters)]
        else:
            return [Polygon(p1, p2, p1_p3, screen=polygon.screen, **polygon.parameters),
                    Polygon(p1_p3, p2, p3, screen=polygon.screen, **polygon.parameters)]

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

def render(pygm, screen:Screen, polygons:list, light:list, steps:bool = True) -> None:
    """
    Set up the scene given the polygons and lights
    """
    pygm.fill((0,0,0))
    polygons = reorganize(polygons, screen)
    if type(steps) == float or type(steps) == int:
        t:float = steps
        steps:bool = True
    else:
        t:float = 0.5/len(polygons)
    for p in polygons:
        if p.see:
            pygame.draw.polygon(pygm, p.color_to_plot, p.positions_screen)
            if steps:
                pygame.display.flip()
                sleep(t)
            for l in light:
                p.add_composition(l)
                if steps:
                    sleep(t)
            pygame.draw.polygon(pygm, p.color_to_plot, p.positions_screen)
            if steps:
                pygame.display.flip()
                sleep(t)
    for l in light:
        pygame.draw.circle(pygm, l.color, l.positions_screen, radius = int(20/(max(l.position[2], 1))**(1/2) + 1))
    pygame.display.flip()
