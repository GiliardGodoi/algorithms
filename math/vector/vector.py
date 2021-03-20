from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Can not normalize the zero vector'
    CANNOT_COMPUTE_AN_ANGLE_WITH_THE_ZERO_VECTOR_MSG = "Cannot compute an angle with the zero vector"
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "No unique pararrel component."
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "No unique orthogonal component."
    CANNOT_CALCULATED_CROSS_PRODUCT_FROM_NO_3D_VECTORS = "No 3D vector. It cannot be calculated."

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)
        except ValueError:
            raise ValueError('The coordinates must be no empty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __len__(self):
        return self.dimension

    def __getitem__(self, i):
        return self.coordinates[i]

    def __add__(self,v):
        return self.plus(v)

    def __sub__(self, v):
        return self.minus(v)

    def __abs__(self):
        return sqrt(self.dot(self))

    def plus(self, v):
        #list comprehennssi
        new_coordinates = [ x+y for x,y in zip(self.coordinates, v.coordinates)]
        #new_coordinates = []
        #n = len(self.coordinates)
        #for i in range(n):
        #   new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [ Decimal(c)*x for x in self.coordinates ]
        return Vector(new_coordinates)

    def magnitude(self):
        squares_coordinates = [x**2 for x in self.coordinates]
        sum_coordinates = sum(squares_coordinates)
        return Decimal(sqrt(sum_coordinates))

    def normalized(self):
        try:
            mag = self.magnitude()
            vetor_unit = self.times_scalar(Decimal('1.0')/mag)
            return vetor_unit
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def inner_product(self, vetor):
        x_coordinates_times_y_coordinates = [x*y for x, y in zip(self.coordinates, vetor.coordinates)]
        sum_coordinates = sum(x_coordinates_times_y_coordinates)
        return sum_coordinates

    def dot(self, v):
        return sum( [x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_rad(self, vetor):
        owner_magnitude = self.magnitude()
        vetor_magnitude = vetor.magnitude()
        inner_product_vector = self.inner_product(vetor)
        angle = 0
        try :
            cosine_angle = inner_product_vector / (owner_magnitude * vetor_magnitude)
            angle = acos(cosine_angle)
            return angle
        except ZeroDivisionError :
            raise Exception('One or both vectors are equal zero')

    def angle_degrees(self,vetor):
        rad = self.angle_rad(vetor)
        angle = (rad * 180) / pi
        return angle

    def angle_with(self, vetor, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = vetor.normalized()
            angle_in_radians = acos(round(float(u1.dot(u2)),4))
            if in_degrees:
                degrees_per_radian = 180./ pi
                return angle_in_radians * degrees_per_radian
            else :
                return angle_in_radians
        except Exception as e :
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_COMPUTE_AN_ANGLE_WITH_THE_ZERO_VECTOR_MSG)
            else:
                raise e

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi)
    
    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)
        except Exception as err :
            if str(err) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else :
                raise Exception()

    def component_orthogonal_to(self, basis):
        try :
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as err :
            if str(err) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG :
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else :
                raise Exception()

    def cross_product(self,vector):
        if self.dimension != 3 or len(vector) != 3 : 
            raise Exception(CANNOT_CALCULATED_CROSS_PRODUCT_FROM_NO_3D_VECTORS)
        return Vector([ ( self.coordinates[1]*vector[2] - vector[1]*self.coordinates[2] ),
                        -(self.coordinates[0]*vector[2] - vector[0]*self.coordinates[2] ),
                         (self.coordinates[0]*vector[1] - vector[0]*self.coordinates[1] ) ])

    def cross(self, vector):
        try:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = vector.coordinates
            new_coordinates = [ y1*z2 - y2*z1 ,
                              -(x1*z2 - x2*z1),
                                x1*y2 - x2*y1 ]
            return Vector(new_coordinates)
        except ValueError as error :
            msg = str(error)
            if msg == 'need more than 2 values to unpack' :
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(vector.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or 
                  msg == 'need more than 1 value to unpack'):
                raise Exception('only defined in two and three dimension')
            else :
                raise error

    def area_of_parallelogram(self, vector) :
        VW = self.cross_product(vector)
        return VW.magnitude()

    def area_of_triangle(self, vector):
        parallelogram = self.area_of_parallelogram(vector)
        return parallelogram / Decimal(2.0)