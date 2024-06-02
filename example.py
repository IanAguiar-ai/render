from render import *

if __name__ == "__main__":
    #Screen:
    width, height = 1080, 720
    screen = Screen((0, 0, 1000), width, height)

    #Polygons:
    ref = .7
    n = 200
    m = 600
    polygons = [Polygon((m, n, m), (n, m, m), (n, n, m), screen = screen, reflection = ref), #f1
                Polygon((m, m, m), (n, m, m), (m, n, m), screen = screen, reflection = ref), #f1
                Polygon((m, n, n), (n, m, n), (n, n, n), screen = screen, reflection = ref), #f2
                Polygon((m, m, n), (n, m, n), (m, n, n), screen = screen, reflection = ref), #f2
                Polygon((m, n, n), (n, n, m), (m, n, m), screen = screen, reflection = ref), #f3
                Polygon((n, n, n), (n, n, m), (m, n, n), screen = screen, reflection = ref), #f3
                Polygon((m, m, n), (n, m, m), (m, m, m), screen = screen, reflection = ref), #f4
                Polygon((n, m, n), (n, m, m), (m, m, n), screen = screen, reflection = ref), #f4
                Polygon((n, m, n), (n, m, m), (n, n, n), screen = screen, reflection = ref), #f5
                Polygon((n, n, n), (n, m, m), (n, n, m), screen = screen, reflection = ref), #f5
                Polygon((m, n, n), (m, m, m), (m, m, n), screen = screen, reflection = ref), #f6
                Polygon((m, n, m), (m, m, m), (m, n, n), screen = screen, reflection = ref)] #f6
 
    polygons = multyple_fast(polygons, times = 5)

    #Light:
    light = [Light((m+100, m+100, m+300), color = (255, 255, 255), intensity = 100, ambient = 0.1)]

    #Render:
    render(screen, polygons, light, steps = True)
