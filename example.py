from render import *

if __name__ == "__main__":
    #Screen:
    width, height = 1080, 720
    screen = Screen((0, 0, 1000), width, height)

    #Polygons:
    ref = 1
    n = 200
    m = 600
    color = None#(10, 10, 250)
    polygons = [Polygon((n, n, m), (n, m, m), (m, n, m), screen = screen, reflection = ref, color = color), #f1
                Polygon((m, n, m), (n, m, m), (m, m, m), screen = screen, reflection = ref, color = color), #f1
                Polygon((m, n, n), (n, m, n), (n, n, n), screen = screen, reflection = ref, color = color), #f2
                Polygon((m, m, n), (n, m, n), (m, n, n), screen = screen, reflection = ref, color = color), #f2
                Polygon((m, n, n), (n, n, m), (m, n, m), screen = screen, reflection = ref, color = color), #f3
                Polygon((n, n, n), (n, n, m), (m, n, n), screen = screen, reflection = ref, color = color), #f3
                Polygon((m, m, n), (n, m, m), (m, m, m), screen = screen, reflection = ref, color = color), #f4
                Polygon((n, m, n), (n, m, m), (m, m, n), screen = screen, reflection = ref, color = color), #f4
                Polygon((n, m, n), (n, m, m), (n, n, n), screen = screen, reflection = ref, color = color), #f5
                Polygon((n, n, n), (n, m, m), (n, n, m), screen = screen, reflection = ref, color = color), #f5
                Polygon((m, m, n), (m, m, m), (m, n, n), screen = screen, reflection = ref, color = color), #f6
                Polygon((m, n, n), (m, m, m), (m, n, m), screen = screen, reflection = ref, color = color)] #f6
 
    polygons = multyple_fast(polygons, times = 2)

    #Light:
    light = [Light([m-100, m-100, 1000], color = (255, 150, 150), intensity = 100, ambient = .5)]

    #Render:
    pygame.init()
    pygm = pygame.display.set_mode((screen.width, screen.height))
    pygame.display.set_caption("RENDER")
    clock = pygame.time.Clock()
    while True:
        for i in range(0, 1000, 10):
            render(pygm, screen, polygons, light, steps = False)
            light[0].position[2] = i
            clock.tick(24)
        for i in range(1000, 0, -10):
            render(pygm, screen, polygons, light, steps = False)
            light[0].position[2] = i
            clock.tick(24)
