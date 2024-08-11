from render import *
from math import cos, sin
from random import random

if __name__ == "__main__":
    #Screen:
    width, height = 1080, 720
    screen = Screen((0, 0, 1000), width, height)

    t_fps = 1

    roug = lambda x: max(0, sin(x*100)/1.5)
    strange = lambda x: x**3

    #Polygons:
    ref = 0.6
    amb = .01
    int_ = 10
    n = 200
    m = 600
    h_0 = 100
    h_1 = 600
    metalic = 3#0.3
    rough = 10#0.5
    dispersion_light = 0.5
    color = (10, 10, 250)
    stats_polygon = {"color":color,
                     "reflection":ref,
                     "metalic":metalic,
                     "rough":rough,
                     "dispersion_light":dispersion_light,
                     "texture":False}

    #Cube:
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

    stats_polygon["color"] = [120, 200, 80]
    #Triangle:
    a = 1000
    b = 700
    c = 900
    d = 1100
    t1 = (a, a, b)
    t2 = (d, b, c)
    t3 = (b, a, c)
    t4 = (a, a, c)
    #polygons.extend([Polygon(t3, t2, t1, screen = screen, **stats_polygon)])

    #stats_polygon["color"] = [255, 255, 255]
    #polygons.extend([Polygon((1200, 100, 1000), (100, 1200, 1000), (100, 100, 1000), screen = screen, **stats_polygon),
    #                 Polygon((1200, 1200, 1000), (100, 1200, 1000), (1200, 100, 1000), screen = screen, **stats_polygon)])
 
    polygons = multyple_fast(polygons, times = 7)

    #Light:
    color_light = (255, 150, 150)
    size = 1
    light = [Light([50, 10, 1000], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
    
    #Render:
    pygame.init()
    pygm = pygame.display.set_mode((screen.width, screen.height))
    pygame.display.set_caption("RENDER")
    clock = pygame.time.Clock()
    render(pygm, screen, polygons, light, steps = False)
    while True:
##        for i in range(10, 500, 5):
##            light = [Light([50, i, 1000], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
##            render(pygm, screen, polygons, light, steps = False)
##            clock.tick(24)
##        print("a")
##        for i in range(500, 10, -5):
##            light = [Light([50, i, 1000], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
##            render(pygm, screen, polygons, light, steps = False)
##            clock.tick(24)
##        print("b")
##        for i in range(1000, 10, -10):
##            light = [Light([50, 10, i], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
##            render(pygm, screen, polygons, light, steps = False)
##            clock.tick(24)
##        print("d")
##        for i in range(10, 500, 5):
##            light = [Light([50, i, 10], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
##            render(pygm, screen, polygons, light, steps = False)
##            clock.tick(24)
##        print("e")
##        for i in range(500, 10, -5):
##            light = [Light([50, i, 10], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
##            render(pygm, screen, polygons, light, steps = False)
##            clock.tick(24)
##        print("f")
  
        mouse_x, mouse_y = 0, 0
        z = 0
        color_r, color_g, color_b = color_light
        n_t = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                z += 1
            if keys[pygame.K_s]:
                z -= 1
            if keys[pygame.K_a]:
                z = 0

            if keys[pygame.K_u]:
                color_r = min(max(0,color_r+1), 255)
            if keys[pygame.K_j]:
                color_r = min(max(0,color_r-1), 255)
            if keys[pygame.K_i]:
                color_g = min(max(0,color_g+1), 255)
            if keys[pygame.K_k]:
                color_g = min(max(0,color_g-1), 255)
            if keys[pygame.K_o]:
                color_b = min(max(0,color_b+1), 255)
            if keys[pygame.K_l]:
                color_b = min(max(0,color_b-1), 255)

            if n_t % 70 == 0:
                n_t = 1
                print(f"Z:{z}\nR:{color_r}\nG:{color_g}\nB:{color_b}")
                print(f"Mean fps: {fps}")
            n_t += 1

            position_light = [mouse_x, mouse_y, z]
            light = [Light(position_light, color = (color_r, color_g, color_b), screen=screen, intensity=int_, ambient=amb, size=size)]
            render(pygm, screen, polygons, light, steps = False, shadows = False)
            clock.tick(24)

            if t_fps == 1:
                fps = clock.get_fps()
            else:
                fps = (clock.get_fps() + (fps*t_fps)) / (t_fps + 1)
            t_fps += 1
            
    pygame.quit()   
