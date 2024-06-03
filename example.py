from render import *

if __name__ == "__main__":
    #Screen:
    width, height = 1080, 720
    screen = Screen((0, 0, 1000), width, height)

    #Polygons:
    ref = 1
    amb = 0.15
    int_ = 1000
    n = 200
    m = 600
    metalic = .3
    rough = .8
    dispersion_light = .6
    color = (10, 10, 250)
    stats_polygon = {"color":color,
                     "reflection":ref,
                     "metalic":metalic,
                     "rough":rough,
                     "dispersion_light":dispersion_light}

    #Cube:
    polygons = [Polygon((n, n, m), (n, m, m), (m, n, m), screen = screen, **stats_polygon), #f1
                Polygon((m, n, m), (n, m, m), (m, m, m), screen = screen, **stats_polygon), #f1
                Polygon((m, n, n), (n, m, n), (n, n, n), screen = screen, **stats_polygon), #f2
                Polygon((m, m, n), (n, m, n), (m, n, n), screen = screen, **stats_polygon), #f2
                Polygon((m, n, n), (n, n, m), (m, n, m), screen = screen, **stats_polygon), #f3
                Polygon((n, n, n), (n, n, m), (m, n, n), screen = screen, **stats_polygon), #f3
                Polygon((m, m, n), (n, m, m), (m, m, m), screen = screen, **stats_polygon), #f4
                Polygon((n, m, n), (n, m, m), (m, m, n), screen = screen, **stats_polygon), #f4
                Polygon((n, m, n), (n, m, m), (n, n, n), screen = screen, **stats_polygon), #f5
                Polygon((n, n, n), (n, m, m), (n, n, m), screen = screen, **stats_polygon), #f5
                Polygon((m, m, n), (m, m, m), (m, n, n), screen = screen, **stats_polygon), #f6
                Polygon((m, n, n), (m, m, m), (m, n, m), screen = screen, **stats_polygon)] #f6

    #Triangle:
##    a = 1000
##    b = 500
##    c = 900
##    d = 1100
##    t1 = (a, a, b)
##    t2 = (d, b, c)
##    t3 = (b, a, c)
##    t4 = (a, a, c)
##    polygons.extend([Polygon(t3, t2, t1, screen = screen, **stats_polygon),
##                     Polygon(t2, t3, t4, screen = screen, **stats_polygon),
##                     Polygon(t1, t3, t4, screen = screen, **stats_polygon),
##                     Polygon(t4, t2, t1, screen = screen, **stats_polygon)])
 
    polygons = multyple_fast(polygons, times = 3)

    #Light:
    color_light = (255, 150, 150)
    size = 1
    light = [Light([50, 10, 1000], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
    
    #Render:
    pygame.init()
    pygm = pygame.display.set_mode((screen.width, screen.height))
    pygame.display.set_caption("RENDER")
    clock = pygame.time.Clock()
    render(pygm, screen, polygons, light, steps = True)
    while True:
        for i in range(10, 500, 5):
            light = [Light([50, i, 1000], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
            render(pygm, screen, polygons, light, steps = False)
            clock.tick(24)
        print("a")
        for i in range(500, 10, -5):
            light = [Light([50, i, 1000], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
            render(pygm, screen, polygons, light, steps = False)
            clock.tick(24)
        print("b")
        for i in range(1000, 10, -10):
            light = [Light([50, 10, i], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
            render(pygm, screen, polygons, light, steps = False)
            clock.tick(24)
        print("d")
        for i in range(10, 500, 5):
            light = [Light([50, i, 10], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
            render(pygm, screen, polygons, light, steps = False)
            clock.tick(24)
        print("e")
        for i in range(500, 10, -5):
            light = [Light([50, i, 10], color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
            render(pygm, screen, polygons, light, steps = False)
            clock.tick(24)
        print("f")
  
        mouse_x, mouse_y = 0, 0
        z = 0
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

            position_light = [mouse_x, mouse_y, z]
            light = [Light(position_light, color=color_light, screen=screen, intensity=int_, ambient=amb, size=size)]
            render(pygm, screen, polygons, light, steps=False)
            clock.tick(24)
            
    pygame.quit()
