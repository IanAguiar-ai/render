from render import *

if __name__ == "__main__":
    #Screen:
    width, height = 1080, 720
    screen = Screen((0, 0, 1000), width, height)

    #Polygons:
    ref = .8
    amb = 0.15
    int_ = 1000
    n = 200
    m = 600
    metalic = .3
    rough = .7
    color = (10, 10, 250)
    polygons = [Polygon((n, n, m), (n, m, m), (m, n, m), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f1
                Polygon((m, n, m), (n, m, m), (m, m, m), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f1
                Polygon((m, n, n), (n, m, n), (n, n, n), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f2
                Polygon((m, m, n), (n, m, n), (m, n, n), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f2
                Polygon((m, n, n), (n, n, m), (m, n, m), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f3
                Polygon((n, n, n), (n, n, m), (m, n, n), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f3
                Polygon((m, m, n), (n, m, m), (m, m, m), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f4
                Polygon((n, m, n), (n, m, m), (m, m, n), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f4
                Polygon((n, m, n), (n, m, m), (n, n, n), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f5
                Polygon((n, n, n), (n, m, m), (n, n, m), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f5
                Polygon((m, m, n), (m, m, m), (m, n, n), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic), #f6
                Polygon((m, n, n), (m, m, m), (m, n, m), screen = screen, reflection = ref, color = color, rough = rough, metalic = metalic)] #f6
 
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
    #render(pygm, screen, polygons, light, steps = True)
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
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
            position_light = [mouse_x, mouse_y, 0]
            light = [Light(position_light, color = color_light, screen = screen, intensity = int_, ambient = amb, size = size)]
            render(pygm, screen, polygons, light, steps = False)
            clock.tick(24)
            
    pygame.quit()
