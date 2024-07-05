"""
Algebra operations
"""

from libc.math cimport sqrt

cpdef vector(a_, b_):
    """
    Calculates the vector given two points
    """
    cdef float[3] a = a_
    cdef float[3] b = b_
    return b[0] - a[0], b[1] - a[1], b[2] - a[2]

cpdef vector_center_polygon(p1_:(float, float, float), p2_:(float, float, float), p3_:(float, float, float)):
    """
    Find the center point of a polygon
    """
    cdef float[3] p1 = p1_
    cdef float[3] p2 = p2_
    cdef float[3] p3 = p3_
    return ((p1[0] + p2[0] + p3[0]) / 3,
            (p1[1] + p2[1] + p3[1]) / 3,
            (p1[2] + p2[2] + p3[2]) / 3)


cpdef vector_vectorial_product(p1_p2_:(float, float, float), p2_p3_:(float, float, float), p1_p3_:(float, float, float)):
    """
    Find vectorial product
    """
    cdef float[3] p1_p2 = p1_p2_
    cdef float[3] p2_p3 = p2_p3_
    cdef float[3] p1_p3 = p1_p3_
    return ((p1_p2[1] * p1_p3[2]) - (p1_p2[2] * p1_p3[1]),
            (p1_p2[2] * p1_p3[0]) - (p1_p2[0] * p1_p3[2]),
            (p1_p2[0] * p1_p3[1]) - (p1_p2[1] * p1_p3[0]))

cpdef dot_product(vector_1_:(float, float, float), vector_2_:(float, float, float)):
    """
    Dot product
    """
    cdef float[3] vector_1 = vector_1_
    cdef float[3] vector_2 = vector_2_
    return sqrt((vector_1[0] * vector_2[0])*(vector_1[0] * vector_2[0]) + \
                (vector_1[1] * vector_2[1])*(vector_1[1] * vector_2[1]) + \
                (vector_1[2] * vector_2[2])*(vector_1[2] * vector_2[2]))

cpdef vectorial_product_vector(a_:(float, float, float), b_:(float, float, float)):
    """
    Find vectorial product
    """
    cdef float[3] a = a_
    cdef float[3] b = b_
    return ((a[1] * b[2]) - (a[2] * b[1]),
            (a[2] * b[0]) - (a[0] * b[2]),
            (a[0] * b[1]) - (a[1] * b[0]))

cpdef project_point(p_, screen_):
    cdef float[3] p = p_
    cdef float[3] screen = screen_
    
    cdef float z_factor = screen[2]
    cdef float scale = z_factor / (z_factor + p[2])
    
    cdef float x = screen[0] + int((p[0] - screen[0]) * scale)
    cdef float y = screen[1] + int((p[1] - screen[1]) * scale)
    return x, y

cpdef normalized(vector_):
    """
    Normalize a vector
    """
    cdef float[3] vector = vector_
    
    cdef float magnitude = sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])
    cdef float[3] vect
    vect[0] = vector[0]/magnitude
    vect[1] = vector[1]/magnitude
    vect[2] = vector[2]/magnitude
    return vect

cpdef distance_two_points_vector(obj_1_, obj_2_):
    """
    Distance two points
    """
    cdef float[3] obj_1 = obj_1_
    cdef float[3] obj_2 = obj_2_
    
    return sqrt((obj_1[0] - obj_2[0])*(obj_1[0] - obj_2[0]) + \
                (obj_1[1] - obj_2[1])*(obj_1[1] - obj_2[1]) + \
                (obj_1[2] - obj_2[2])*(obj_1[2] - obj_2[2]))
