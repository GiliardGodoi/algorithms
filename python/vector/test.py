import unittest as ut
import math
from decimal import Decimal
from vector import Vector
from line import Line
from plane import Plane

class VectorTest(ut.TestCase):

    def test_construct_vector(self):
        v1 = Vector([2,3,5])
        self.assertIsNotNone(v1)
        self.assertIsInstance(v1,Vector)
        
        with self.assertRaises(TypeError) as err :
            v2 = Vector()
        
        with self.assertRaises(Exception) as err :
            v3 = Vector({'a' : 4, 'b': 5, 'c' : 6})
            w = Vector("abracadabra")
        
        with self.assertRaises(ValueError) as err :
            v4 = Vector([])

    def test_plus(self):
        v1 = Vector([1,2,3])
        v2 = Vector([2, 2, 2])
        v3 = v1 + v2
        self.assertEqual(v3,Vector([3,4,5]))

    def test_minus(self):
        v = Vector([1.0, 2.0, 3.0, 4.0])
        w = Vector([5.0, 2.0, 4.0, 1.0])
        self.assertEqual(v-w,Vector([-4,0,-1,3]))

    def test_len(self):
        z = Vector([10000])
        self.assertEqual(len(z), 1)

        y = Vector([-4,-3])
        self.assertEqual(len(y), 2)

        x = Vector([0,0,0])
        self.assertEqual(len(x), 3)
        
        w = Vector([5.0, 2.0, 4.0, 1.0])
        self.assertEqual(len(w), 4)

    def test_abs(self):
        v = Vector([0,1,0])
        self.assertEqual(abs(v),1)

    def test_getitem(self):
        v1 = Vector([9,8,7])
        self.assertEqual(v1[0],9)
        self.assertEqual(v1[1],8)
        self.assertEqual(v1[2],7)

    def test_angles_degree(self):
        v = Vector([1,0,0])
        w = Vector([0,1,0])
        self.assertEqual(v.angle_degrees(w),90)
        self.assertEqual(v.angle_degrees(v),0)

        t = Vector([0,0,0])
        with self.assertRaises(Exception) as cm:
            v.angle_degrees(t)

    def test_rad_angles(self):
        v = Vector([1,0,0])
        w = Vector([0,1,0])
        self.assertEqual(v.angle_rad(w),(math.pi/2))
        self.assertEqual(w.angle_rad(w),0)

        t = Vector([0,0,0])
        with self.assertRaises(Exception) as cm:
            v.angle_rad(t)

    def test_angle_with(self):
        v = Vector([1,0,0])
        w = Vector([0,1,0])
        self.assertEqual(v.angle_with(w),(math.pi/2))
        self.assertEqual(v.angle_with(w,in_degrees=True),90)

        t = Vector([0,0,0])
        with self.assertRaises(Exception) as cm:
            v.angle_rad(t)

    def test_is_zero(self):
        v1 = Vector([0,0,0])
        self.assertTrue(v1.is_zero())

        v2 = Vector([0,1,0])
        self.assertFalse(v2.is_zero())
    
    def test_times_scalar(self):
        xCoords = [1.0, 2.0, 3.0, 4.0]
        yCoords = [5.0, 2.0, 4.0, 1.0]
        x = Vector(xCoords)
        y = Vector(yCoords)
        self.assertEqual(x.times_scalar(10), Vector([10,20,30,40]))
        self.assertEqual(y.times_scalar(10), Vector([50,20,40,10]))

    def test_dot_product_with_zeror_vector(self):
        v = Vector([0, 0, 0])
        w = Vector([1, 2, 3])
        self.assertEqual(v.dot(w),0)

    def test_dot_product(self):
        v1 = Vector([2,3,4])
        v2 = Vector([2,5,8])
        self.assertEqual(v1.dot(v2), 51)

    def test_parallel_or_orthogonal(self):
        v1 = Vector([-7.579, -7.88])
        w1 = Vector([22.737, 23.64])
        self.assertTrue(v1.is_parallel_to(w1))
        self.assertFalse(v1.is_orthogonal_to(w1))
        self.assertEqual(v1.angle_with(w1,in_degrees=True),180)

        v2 = Vector([-2.029, 9.97, 4.172])
        w2 = Vector([-9.231, -6.639, -7.724])
        self.assertFalse(v2.is_parallel_to(w2))
        self.assertFalse(v2.is_orthogonal_to(w2))
        self.assertNotEqual(v2.angle_with(w2, in_degrees=True),0)
        self.assertNotEqual(v2.angle_with(w2, in_degrees=True),90)

        v3 = Vector([-2.328, -7.284, -1.214])
        w3 = Vector([-1.821, 1.072, -2.94])
        self.assertFalse(v3.is_parallel_to(w3))
        self.assertTrue(v3.is_orthogonal_to(w3))
        self.assertEqual(v3.angle_with(w3, in_degrees=True),90)

        v4 = Vector([2.118, 4.827])
        w4 = Vector([0,0])
        self.assertTrue(v4.is_parallel_to(w4))
        self.assertTrue(v4.is_orthogonal_to(w4))
        with self.assertRaises(Exception) as expt :
            v4.angle_with(w4,in_degrees=True)

    def test_magnitude_with_vector_normalized(self):
        v1 = Vector([-0.221, 7.437])
        u1 = v1.normalized()
        self.assertAlmostEqual(v1.magnitude(),Decimal(7.440282925),places=9)
        self.assertAlmostEqual(u1.magnitude(),Decimal(1.0))

        v2 = Vector([8.813, -1.331, -6.247])
        u2 = v2.normalized()
        self.assertAlmostEqual(v2.magnitude(),Decimal(10.88418757),places=8)
        self.assertAlmostEqual(u2.magnitude(),Decimal(1.0))

        v3 = Vector([5.581, -2.136])
        u3 = v3.normalized()
        self.assertAlmostEqual(v3.magnitude(),Decimal(5.975789237),places=9)
        self.assertAlmostEqual(u2.magnitude(),Decimal(1.0))

        v4 = Vector([1.996, 3.108, -4.554])
        u4 = v4.normalized()
        self.assertAlmostEqual(v4.magnitude(),Decimal(5.863667453),places=9)
        self.assertAlmostEqual(u4.magnitude(),Decimal(1.0))

    def dot_product_and_angle(self):
        v1 = Vector([7.887, 4.138])
        w1 = Vector([-8.802, 6.776])

        v2 = Vector([-5.955, -4.904, -1.874])
        w2 = Vector([-4.496, -8.755, 7.103])

        v3 = Vector([3.183, -7.627])
        w3 = Vector([-2.669, 5.319])

        v4 = Vector([7.35, 0.221, 5.188])
        w4 = Vector([2.751, 8.259, 3.985])

    def test_component_parallel_and_component_orthogonal(self):
        v = Vector([3.039 , 1.879])
        b = Vector([0.825, 2.036])
        self.assertAlmostEqual(v.component_parallel_to(b),Vector([1.083, 2.672]), places=3)

        v = Vector([-9.88, -3.264, -8.159])
        b = Vector([-2.155, -9.353, -9.473])
        self.assertAlmostEqual(v.component_orthogonal_to(b), Vector([-8.350, 3.376, -1.434]),places=3)

        v = Vector([3.009, -6.172, 3.692, -2.51])
        b = Vector([6.404, -9.144, 2.759, 8.718])
        p = v.component_parallel_to(b)
        t = v.component_orthogonal_to(b)
        self.assertAlmostEqual((p+t),v,places=3)

    def test_cross_product(self):
        X = Vector([8.462, 7.893, -8.187])
        W = Vector([6.984, -5.975, 4.778])
        XW = X.cross_product(W)
        self.assertAlmostEqual(XW,Vector([-11.204570000, -97.609440000, -105.685160000]),places=5)

        t = Vector([9.32, 4.3232])
        with self.assertRaises(Exception) as exe :
            X.cross_product(t)
    
    def test_cross_product_with_zero_vector(self):
        X = Vector([8.462, 7.893, -8.187])
        Z = Vector([0,0,0])
        self.assertAlmostEqual(X.cross_product(Z), Vector([0,0,0]))

    def test_cross_product_with_parallel_vectors(self):
        v1 = Vector([2.54, 3.96, 9.874 ])
        w1 = Vector([17.78, 27.72, 69.118])
        self.assertAlmostEqual(v1.cross_product(w1), Vector([0,0,0]))

    def test_area_of_parallelogram(self):
        X = Vector([8.462, 7.893, -8.187])
        W = Vector([6.984, -5.975, 4.778])
        self.assertAlmostEqual(X.area_of_parallelogram(W),Decimal(144.30000),places=3)
    
    def test_area_of_triangle(self):
        X = Vector([8.462, 7.893, -8.187])
        W = Vector([6.984, -5.975, 4.778])
        self.assertAlmostEqual(X.area_of_triangle(W),Decimal(72.15001422), places=3)

class LineTest(ut.TestCase):

    def test_is_parallel_to(self):
        l1 = Line(normal_vector=Vector([3,-2]),constant_term=1)
        l2 = Line(normal_vector=Vector([-6,4]),constant_term=0)
        self.assertTrue(l1.is_parallel_to(l2))

        l3 = Line(normal_vector=Vector([1,2]),constant_term=3)
        l4 = Line(normal_vector=Vector([1,-1]),constant_term=2)
        self.assertFalse(l3.is_parallel_to(l4))
    
    def test_evaluate(self):
        l1 = Line(normal_vector=Vector([3,-2]),constant_term=1)
        self.assertAlmostEqual(l1.evaluate([5,5]),5)

    def test_equal(self):
        l1 = Line(normal_vector=Vector([4.046,2.836]),constant_term=1.21)
        l2 = Line(normal_vector=Vector([10.115,7.09]),constant_term=3.025)
        self.assertEqual(l1,l2)

    def test_not_equal(self):
        l1 = Line(normal_vector=Vector([7.204,3.182]),constant_term=8.68)
        l2 = Line(normal_vector=Vector([8.172,4.114]),constant_term=9.883)
        self.assertNotEqual(l1,l2)

    def test_intersection(self):
        l1 = Line(normal_vector=Vector([7.204,3.182]),constant_term=8.68)
        l2 = Line(normal_vector=Vector([8.172,4.114]),constant_term=9.883)
        x,y = l1.intersection(l2)
        self.assertAlmostEqual(x,Decimal(1.173),places=3)
        self.assertAlmostEqual(y,Decimal(0.073),places=3)
    
    def test_not_intersection(self):
        l1 = Line(normal_vector=Vector([1.182,5.562]),constant_term=6.744)
        l2 = Line(normal_vector=Vector([1.773, 8.343]),constant_term=9.525)
        self.assertIsNone(l1.intersection(l2))

class PlaneTest(ut.TestCase):

    def test_is_parallel_to(self):
        plane1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
        plane2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)
        self.assertTrue(plane1.is_parallel_to(plane2))
        self.assertEqual(plane1, plane2)

        plane3 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
        plane4 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)
        self.assertFalse(plane3.is_parallel_to(plane4))
        self.assertNotEqual(plane3, plane4)

        plane5 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
        plane6 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)
        self.assertTrue(plane5.is_parallel_to(plane6))
        self.assertNotEqual(plane5, plane6)

if __name__ == "__main__" :
    ut.main()