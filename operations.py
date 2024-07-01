"""
Algebra operations
"""

def vector(a:(float, float, float), b:(float, float, float)) -> (float, float, float):
    """
    Calculates the vector given two points
    """
    return b[0] - a[0], b[1] - a[1], b[2] - a[2]

def center_polygon(polygon:"Polygon") -> (float, float, float):
    """
    Find the center point of a polygon
    """      
    return ((polygon.p1[0] + polygon.p2[0] + polygon.p3[0]) / 3,
            (polygon.p1[1] + polygon.p2[1] + polygon.p3[1]) / 3,
            (polygon.p1[2] + polygon.p2[2] + polygon.p3[2]) / 3)

def vectorial_product(a:"Polygon") -> (float, float, float):
    """
    Find vectorial product
    """
    return ((a.p1_p2[1] * a.p1_p3[2]) - (a.p1_p2[2] * a.p1_p3[1]),
            (a.p1_p2[2] * a.p1_p3[0]) - (a.p1_p2[0] * a.p1_p3[2]),
            (a.p1_p2[0] * a.p1_p3[1]) - (a.p1_p2[1] * a.p1_p3[0]))

def vectorial_product_vector(a:(float, float, float), b:(float, float, float)) -> (float, float, float):
    """
    Find vectorial product
    """
    return ((a[1] * b[2]) - (a[2] * b[1]),
            (a[2] * b[0]) - (a[0] * b[2]),
            (a[0] * b[1]) - (a[1] * b[0]))

def dot_product(vector_1:(float, float, float), vector_2:(float, float, float)) -> float:
    """
    Dot product
    """
    return ((vector_1[0] * vector_2[0])**2 + \
            (vector_1[1] * vector_2[1])**2 + \
            (vector_1[2] * vector_2[2])**2)**(1/2)

def find_normal_vector(polygon:"Polygon") -> (float, float, float):
    """
    Find the normal vector
    """
    vectorial:(float, float, float) = vectorial_product(polygon)                
    normalized:float =  (vectorial[0]**2 + vectorial[1]**2 + vectorial[2]**2)**(1/2)        
    return (vectorial[0]/normalized, vectorial[1]/normalized, vectorial[2]/normalized)

def project_point(p:(float, float, float), screen:"Screen") -> (float, float):
        z_factor:float = screen.position[2]
        scale:float = z_factor / (z_factor + p[2])
        
        x:float = screen.position[0] + int((p[0] - screen.position[0]) * scale)
        y:float = screen.position[1] + int((p[1] - screen.position[1]) * scale)
        return x, y

def transpose_on_screen(polygon:"Polygon", screen:"Screen") -> ((float, float), (float, float), (float, float)):
    """
    Transpose polygon on 2d screen (x, y) considering perspective projection
    """
    #print(dir(polygon))
    p1_2d:(float, float) = project_point(polygon.p1, screen)
    p2_2d:(float, float) = project_point(polygon.p2, screen)
    p3_2d:(float, float) = project_point(polygon.p3, screen)
    return p1_2d, p2_2d, p3_2d

def transpose_light_on_screen(light:"Light", screen:"Screen") -> ((float, float), (float, float), (float, float)):
    """
    Transpose polygon on 2d screen (x, y) considering perspective projection
    """
    return project_point(light.position, screen)

def normalized(vector:(float, float, float)) -> (float, float, float):
    """
    Normalize a vector
    """
    magnitude:float = (vector[0]**2 + vector[1]**2 + vector[2]**2)**(1/2)
    return (vector[0]/magnitude, vector[1]/magnitude, vector[2]/magnitude)

def distance_two_points(obj_1:"obj", obj_2:"obj") -> float:
    """
    Distance two objects
    """
    return ((obj_1.position[0] - obj_2.position[0])*(obj_1.position[0] - obj_2.position[0]) + \
            (obj_1.position[1] - obj_2.position[1])*(obj_1.position[1] - obj_2.position[1]) + \
            (obj_1.position[2] - obj_2.position[2])*(obj_1.position[2] - obj_2.position[2]))**(1/2)

def distance_two_points_vector(obj_1:(float, float, float), obj_2:(float, float, float)) -> float:
    """
    Distance two points
    """
    return ((obj_1[0] - obj_2[0])*(obj_1[0] - obj_2[0]) + \
            (obj_1[1] - obj_2[1])*(obj_1[1] - obj_2[1]) + \
            (obj_1[2] - obj_2[2])*(obj_1[2] - obj_2[2]))**(1/2)

def light_in_polygon(polygon:"Polygon", light:"Light", screen:"Screen") -> (int, int, int):
    """
    Performs the light operation on the object
    """

    #Normalize colors:
    light_normalized:[float, float, float] = [light.color[0]/255,
                                              light.color[1]/255,
                                              light.color[2]/255]

    polygon_normalized:[float, float, float] = [polygon.color[0]/255,
                                                polygon.color[1]/255,
                                                polygon.color[2]/255]

    #Calculate distance for intensity:
    distance:float = distance_two_points(polygon, light)
    intensity:float = 1/(distance**(1/light.intensity))

    #Calculate exposition of polygon to light:
    light_vector:(float, float, float) = normalized(vector(light.position, polygon.position))
    exposition:float = light_vector[0] * polygon.normal_vector[0] + \
                       light_vector[1] * polygon.normal_vector[1] + \
                       light_vector[2] * polygon.normal_vector[2] #Also the dot product

    if exposition > 0.95:
        polygon.in_light = True

    #Calculate reflection of light:
    reflection_vector:(float, float, float) = [light_vector[0] - 2 * exposition * polygon.normal_vector[0],
                                               light_vector[1] - 2 * exposition * polygon.normal_vector[1],
                                               light_vector[2] - 2 * exposition * polygon.normal_vector[2]] #R_line, way 1 to calc
    camera_vector:(float, float, float) = normalized(vector(screen.position, polygon.position)) #w_0
    reflection:float = dot_product(reflection_vector, camera_vector) * intensity #w*R, way 1 to calc
##    reflection_vector:(float, float, float) = vectorial_product_vector(camera_vector, light_vector) #Other way to calc
##    reflection:float = dot_product(reflection_vector, polygon.normal_vector)
    
    if polygon.texture != False:
        reflection = polygon.texture(reflection)
    reflection = reflection**polygon.dispersion_light * polygon.rough + exposition * polygon.metalic  

    #print(f"lv: {light_vector} <- {polygon.normal_vector}")
    #print(f"Exposition: {exposition}")
    #print(f"Reflection: {reflection}")

    #Calculate color:
    correct:int = lambda x: int(max(0, min(x*255, 255)))
    new_color:[float, float, float] = [((max(exposition * (1 + intensity), light.ambient) * polygon_normalized[i] * light_normalized[i]) + 
                                       (light_normalized[i]*reflection**(5)*polygon.reflection))/2 for i in range(3)]
    return (correct(new_color[0]),
            correct(new_color[1]),
            correct(new_color[2]))

def shadow_in_polygon(polygon:"Polygon", light:"Light", polygon_:"Polygon"):
    shadow = dot_product(vector(polygon_.position, light.position),
                         vector(polygon.position, light.position))
    if shadow > 780_000:
        shadow -= 780_000
        return [max(0, light.ambient*shadow/100_000 + polygon.color_to_plot[i]*(1 - shadow/100_000)) for i in range(3)]
    else:
        return polygon.color_to_plot


# =====================================================================================================================
"""
If have a cython pre-compiled functions
"""

#Try export functions pre compiled
try_cython = True

if try_cython: 
    cython_ = 0
    try:
        from operations_cython import vector, vector_center_polygon, \
             vector_vectorial_product, dot_product, vectorial_product_vector, \
             project_point, normalized, distance_two_points_vector
        print("OTIMIZED FUNCTIONS CYTHON")
        cython_ = 1
    except:
        pass

    if cython_:
        def center_polygon(polygon:"Polygon") -> (float, float, float):
            """
            Find the center point of a polygon
            """      
            return vector_center_polygon(polygon.p1, polygon.p2, polygon.p3)

        def vectorial_product(a:"Polygon") -> (float, float, float):
            """
            Find vectorial product
            """
            return vector_vectorial_product(a.p1_p2, a.p2_p3, a.p1_p3)

        def transpose_on_screen(polygon:"Polygon", screen:"Screen") -> ((float, float), (float, float), (float, float)):
            """
            Transpose polygon on 2d screen (x, y) considering perspective projection
            """
            #print(dir(polygon))
            p1_2d:(float, float) = project_point(polygon.p1, screen.position)
            p2_2d:(float, float) = project_point(polygon.p2, screen.position)
            p3_2d:(float, float) = project_point(polygon.p3, screen.position)
            return p1_2d, p2_2d, p3_2d

        def transpose_light_on_screen(light:"Light", screen:"Screen") -> ((float, float), (float, float), (float, float)):
            """
            Transpose polygon on 2d screen (x, y) considering perspective projection
            """
            return project_point(light.position, screen.position)

        def distance_two_points(obj_1:"obj", obj_2:"obj") -> float:
            """
            Distance two objects
            """
            return distance_two_points_vector(obj_1.position, obj_2.position)
