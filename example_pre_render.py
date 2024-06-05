import pygame
from render import *
from math import cos, sin
from random import random

def save_frames_to_memory(min_frames=400):
    frames = []

    # Configuração da tela
    width, height = 1080, 720
    screen = Screen((0, 0, 1000), width, height)

    roug = lambda x: max(0, sin(x*100)/1.5)
    strange = lambda x: x**3

    # Parâmetros dos polígonos
    ref = 1
    amb = 0.05
    int_ = 1000
    n = 200
    m = 600
    h_0 = 200
    h_1 = 600
    metalic = .3
    rough = .7
    dispersion_light = 2
    color = (10, 10, 250)
    stats_polygon = {"color":color,
                     "reflection":ref,
                     "metalic":metalic,
                     "rough":rough,
                     "dispersion_light":dispersion_light,
                     "texture":False}

    # Cubo
    polygons = [Polygon((n, n, h_1), (n, m, h_1), (m, n, h_1), screen = screen, **stats_polygon), #f1
                Polygon((m, n, h_1), (n, m, h_1), (m, m, h_1), screen = screen, **stats_polygon), #f1
                Polygon((m, n, h_0), (n, m, h_0), (n, n, h_0), screen = screen, **stats_polygon), #f2
                Polygon((m, m, h_0), (n, m, h_0), (m, n, h_0), screen = screen, **stats_polygon), #f2
                Polygon((m, n, h_0), (n, n, h_1), (m, n, h_1), screen = screen, **stats_polygon), #f3
                Polygon((n, n, h_0), (n, n, h_1), (m, n, h_0), screen = screen, **stats_polygon), #f3
                Polygon((m, m, h_0), (n, m, h_1), (m, m, h_1), screen = screen, **stats_polygon), #f4
                Polygon((n, m, h_0), (n, m, h_1), (m, m, h_0), screen = screen, **stats_polygon), #f4
                Polygon((n, m, h_0), (n, m, h_1), (n, n, h_0), screen = screen, **stats_polygon), #f5
                Polygon((n, n, h_0), (n, m, h_1), (n, n, h_1), screen = screen, **stats_polygon), #f5
                Polygon((m, m, h_0), (m, m, h_1), (m, n, h_0), screen = screen, **stats_polygon), #f6
                Polygon((m, n, h_0), (m, m, h_1), (m, n, h_1), screen = screen, **stats_polygon)] #f6

    # Triângulo
    a = 1000
    b = 700
    c = 900
    d = 1100
    t1 = (a, a, b)
    t2 = (d, b, c)
    t3 = (b, a, c)
    t4 = (a, a, c)
    polygons.extend([Polygon(t3, t2, t1, screen = screen, **stats_polygon),
                     Polygon(t2, t3, t4, screen = screen, **stats_polygon),
                     Polygon(t1, t3, t4, screen = screen, **stats_polygon),
                     Polygon(t4, t2, t1, screen = screen, **stats_polygon)])
 
    polygons = multyple_fast(polygons, times = 6)

    # Luz
    color_light = (255, 150, 150)
    size = 1
    light_position = [50, 10, 1000]
    light = [Light(light_position, color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
    
    # Inicialização do Pygame
    pygame.init()
    pygm = pygame.display.set_mode((screen.width, screen.height))
    pygame.display.set_caption("RENDER")
    clock = pygame.time.Clock()

    frame_surface = []
    for i in range(10, 500, 5):
        light = [Light([50, i, 1000], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
        render(pygm, screen, polygons, light, steps = False)
        frame_surface = pygm.copy()
        frames.append(frame_surface)
        clock.tick(24)
    
    for i in range(500, 10, -5):
        light = [Light([50, i, 1000], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
        render(pygm, screen, polygons, light, steps = False)
        frame_surface = pygm.copy()
        frames.append(frame_surface)
        clock.tick(24)
    
    for i in range(1000, 10, -10):
        light = [Light([50, 10, i], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
        render(pygm, screen, polygons, light, steps = False)
        frame_surface = pygm.copy()
        frames.append(frame_surface)
        clock.tick(24)
    
    for i in range(10, 500, 5):
        light = [Light([50, i, 10], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
        render(pygm, screen, polygons, light, steps = False)
        frame_surface = pygm.copy()
        frames.append(frame_surface)
        clock.tick(24)
    
    for i in range(500, 10, -5):
        light = [Light([50, i, 10], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
        render(pygm, screen, polygons, light, steps = False)
        frame_surface = pygm.copy()
        frames.append(frame_surface)
        clock.tick(24)

    return frames

def display_frames_from_memory(frames, min_frames=24):
    # Inicialização do Pygame
    pygame.init()
    pygm = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("RENDER")
    clock = pygame.time.Clock()

    frame = 0
    while True:
        for frame_surface in frames:
            pygm.blit(frame_surface, (0, 0))
            pygame.display.flip()
            clock.tick(24)
            frame += 1
            if frame >= len(frames):
                frame = 0

if __name__ == "__main__":
    frames = save_frames_to_memory()  # Pré-renderizar e salvar os quadros na memória
    display_frames_from_memory(frames)  # Exibir os quadros
