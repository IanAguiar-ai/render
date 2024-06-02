from render import *

if __name__ == "__main__":
    #Screen:
    width, height = 1080, 720
    screen = Screen((0, 0, 1000), width, height)

    #Polygons:
    ref = 1
    n = 200
    m = 600
    color = (10, 10, 250)#None
    polygons = [Polygon((m, n, m), (n, m, m), (n, n, m), screen = screen, reflection = ref, color = color), #f1
                Polygon((m, m, m), (n, m, m), (m, n, m), screen = screen, reflection = ref, color = color), #f1
                Polygon((m, n, n), (n, m, n), (n, n, n), screen = screen, reflection = ref, color = color), #f2
                Polygon((m, m, n), (n, m, n), (m, n, n), screen = screen, reflection = ref, color = color), #f2
                Polygon((m, n, n), (n, n, m), (m, n, m), screen = screen, reflection = ref, color = color), #f3
                Polygon((n, n, n), (n, n, m), (m, n, n), screen = screen, reflection = ref, color = color), #f3
                Polygon((m, m, n), (n, m, m), (m, m, m), screen = screen, reflection = ref, color = color), #f4
                Polygon((n, m, n), (n, m, m), (m, m, n), screen = screen, reflection = ref, color = color), #f4
                Polygon((n, m, n), (n, m, m), (n, n, n), screen = screen, reflection = ref, color = color), #f5
                Polygon((n, n, n), (n, m, m), (n, n, m), screen = screen, reflection = ref, color = color), #f5
                Polygon((m, n, n), (m, m, m), (m, m, n), screen = screen, reflection = ref, color = color), #f6
                Polygon((m, n, m), (m, m, m), (m, n, n), screen = screen, reflection = ref, color = color)] #f6
 
    polygons = multyple_fast(polygons, times = 5)

    #Light:
    light = [Light((m-100, m-100, 1000), color = (255, 150, 150), intensity = 100, ambient = .1)]

    #Render:
    render(screen, polygons, light, steps = True)
