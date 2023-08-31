import lib_vect_mat as lvm
import unittest

class TestvectmatOperations (unittest.TestCase):

    def test_add_vect(self):
        result = lvm.add_vect(v1=[1+2j,2+2j,3j],v2=[3+2j,2+2j,1j])
        self.assertAlmostEqual(result, [4.+4.j, -3.+4.j, -9.+4.j])

        result = lvm.add_vect(v1=[3+1j,4+4j,2j],v2=[3+5j,2+2j,4j])
        self.assertAlmostEqual(result, [6.+6.j, 6.+6.j, 0.+6.j])

    def test_invad_vect(self):
        result = lvm.invad_vect(v=[2+8j,3+4j,9-4j])
        self.assertAlmostEqual(result, [-2.-8.j, -3.-4.j, -9.+4.j])

        result = lvm.invad_vect(v=[1+9j,2+5j,11-2j])
        self.assertAlmostEqual(result, [ -1.-9.j,  -2.-5.j, -11.+2.j])
    
    def test_esc_vect(self):
        result = lvm.esc_vect(e=5,v=[-1+5j,7+2j,3-1j])
        self.assertAlmostEqual(result, [-5.+25.j, 35.+10.j, 15.-5.j])

        result = lvm.esc_vect(e=9,v=[-3+7j,1+6j,4-9j])
        self.assertAlmostEqual(result, [-27.+63.j,   9.+54.j,  36.-81.j])

    def test_add_matr(self):
        result = lvm.add_matr(m1=[[1+2j,2-2j,-3j],[3,2j,7+1j]],m2=[[3-2j,-2+5j,1j],[1+1j,2,3-1j]])
        self.assertAlmostEqual(result, [[4.+0.j,  0.+3.j,  0.-2.j],[ 4.+1.j,  2.+2.j, 10.+0.j]])

        result = lvm.add_matr(m1=[[2+3j,5-5j,-4j],[6,5j,9+1j]],m2=[[2-3j,-8+5j,10j],[3+3j,1,4-8j]])
        self.assertAlmostEqual(result, [[ 4.+0.j, -3.+0.j,  0.+6.j],[ 9.+3.j,  1.+5.j, 13.-7.j]])

    def test_invad_matr(self):
        result = lvm.invad_matr(m=[[1+2j,2-2j,-3j],[3,2j,7+1j]])
        self.assertAlmostEqual(result,[[-1.-2.j, -2.+2.j,  0.+3.j],[-3.+0.j, -0.-2.j, -7.-1.j]] )

        result = lvm.invad_matr(m=[[2+8j,6-6j,-12j],[7,9j,1+11j]])
        self.assertAlmostEqual(result, [[-2. -8.j, -6. +6.j,  0.+12.j],[-7. +0.j, -0. -9.j, -1.-11.j]])
    
    def test_esc_matr(self):
        result = lvm.esc_matr(e=5,m=[[3-2j,-2+5j,1j],[1+1j,2,3-1j]])
        self.assertAlmostEqual(result, [[ 15.-10.j, -10.+25.j,   0. +5.j],[  5. +5.j,  10. +0.j,  15. -5.j]])

        result = lvm.esc_matr(e=9,m=[[3-2j,-2+5j,1j],[1+1j,2,3-1j]])
        self.assertAlmostEqual(result, [[ 27.-18.j, -18.+45.j,   0. +9.j],[  9. +9.j,  18. +0.j,  27. -9.j]])

    def test_transp(self):
        result = lvm.transp(a=[[1+2j,2-2j,-3j],[3,2j,7+1j],[3-2j,-2+5j,1j]])
        self.assertAlmostEqual(result, [[ 1.+2.j,  3.+0.j,  3.-2.j],[ 2.-2.j,  0.+2.j, -2.+5.j],[-0.-3.j,  7.+1.j,  0.+1.j]])

        result = lvm.transp(a=[[2+1j,2-2j,-6j],[2,3j,1+7j],[2-3j,-5+2j,9j]])
        self.assertAlmostEqual(result, [[ 2.+1.j,  2.+0.j,  2.-3.j],[ 2.-2.j,  0.+3.j, -5.+2.j],[-0.-6.j,  1.+7.j,  0.+9.j]])

    def test_conjug(self):
        result = lvm.conjug(a=[-2+4j,3-1j,8j])
        self.assertAlmostEqual(result, [-2.-4.j,  3.+1.j,  0.-8.j])

        result = lvm.conjug(a=[-4+2j,1-3j,2j])
        self.assertAlmostEqual(result, [-4.-2.j,  1.+3.j,  0.-2.j])


if __name__ == '__main__':
    unittest.main()