"""
Algebra operations
"""

cpdef vector(float[3] a, float[3] b):
    """
    Calculates the vector given two points
    """
    return b[0] - a[0], b[1] - a[1], b[2] - a[2]

def center_polygon(polygon:"Polygon") -> (float, float, float):
    """
    Find the center point of a polygon
    """      
    return vector_center_polygon(polygon.p1, polygon.p2, polygon.p3)

cpdef vector_center_polygon(float[3] p1:(float, float, float), float[3] p2:(float, float, float), float[3] p3:(float, float, float)) -> (float, float, float):
    """
    Find the center point of a polygon
    """
    return ((p1[0] + p2[0] + p3[0]) / 3,
            (p1[1] + p2[1] + p3[1]) / 3,
            (p1[2] + p2[2] + p3[2]) / 3)

def vectorial_product(a:"Polygon") -> (float, float, float):
    """
    Find vectorial product
    """
    return vector_vectorial_product(a.p1_p2, a.p2_p3, a.p1_p3)

cpdef vector_vectorial_product(float[3] p1_p2:(float, float, float), float[3] p2_p3:(float, float, float), float[3] p1_p3:(float, float, float)) -> (float, float, float):
    """
    Find vectorial product
    """
    return ((p1_p2[1] * p1_p3[2]) - (p1_p2[2] * p1_p3[1]),
            (p1_p2[2] * p1_p3[0]) - (p1_p2[0] * p1_p3[2]),
            (p1_p2[0] * p1_p3[1]) - (p1_p2[1] * p1_p3[0]))

cpdef vectorial_product_vector(float[3] a:(float, float, float), float[3] b:(float, float, float)) -> (float, float, float):
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

def transpose_on_screen(polygon:"Polygon", screen:"Screen") -> ((float, float), (float, float), (float, float)):
    """
    Transpose polygon on 2d screen (x, y) considering perspective projection
    """
    p1_2d:(float, float) = project_point(polygon.p1, screen.position)
    p2_2d:(float, float) = project_point(polygon.p2, screen.position)
    p3_2d:(float, float) = project_point(polygon.p3, screen.position)
    return p1_2d, p2_2d, p3_2d

cpdef project_point(float[3] p, float[3] screen) -> (float, float):
    cdef float z_factor = screen[2]
    cdef float scale = z_factor / (z_factor + p[2])
    
    cdef float x = screen[0] + int((p[0] - screen[0]) * scale)
    cdef float y = screen[1] + int((p[1] - screen[1]) * scale)
    return x, y

def transpose_light_on_screen(light:"Light", screen:"Screen") -> ((float, float), (float, float), (float, float)):
    """
    Transpose polygon on 2d screen (x, y) considering perspective projection
    """
    return project_point(light.position, screen.position)

cpdef normalized(float[3] vector) -> (float, float, float):
    """
    Normalize a vector
    """
    cdef float magnitude = (vector[0]**2 + vector[1]**2 + vector[2]**2)**(1/2)
    cdef float[3] vect
    vect[0] = vector[0]/magnitude
    vect[1] = vector[1]/magnitude
    vect[2] = vector[2]/magnitude
    return vect

def distance_two_points(obj_1:"obj", obj_2:"obj") -> float:
    """
    Distance two objects
    """
    return vectorial_distance_two_points(obj_1.position, obj_2.position)

cpdef distance_two_points_vector(float[3] obj_1, float[3] obj_2) -> float:
    """
    Distance two points
    """
    return ((obj_1[0] - obj_2[0])**2 + \
            (obj_1[1] - obj_2[1])**2 + \
            (obj_1[2] - obj_2[2])**2)**(1/2)
