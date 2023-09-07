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
    ###Continuación pruebas libreria
    def test_daga(self):
        result = lvm.daga(a=[[2+1j,2-2j,-6j],[2,3j,1+7j],[2-3j,-5+2j,9j]])
        self.assertAlmostEqual(result, [[2.-1.j,2.-0.j,2.+3.j],[2.+2.j,0.-3.j,-5.-2.j],[-0.+6.j,1.-7.j,0.-9.j]])

        result = lvm.daga(a=[[2+8j,3j,-1+1j],[1j,0,-3j],[3-5j,-7,4+1j]])
        self.assertAlmostEqual(result, [[2.-8.j,0.-1.j,3.+5.j],[0.-3.j,0.-0.j,-7.-0.j],[-1.-1.j,-0.+3.j,4.-1.j]])
    def test_prod_mat(self):
        result = lvm.prod_mat(a=[[2+1j,2-2j,-6j],[2,3j,1+7j],[2-3j,-5+2j,9j]],b=[[2-3j,-8+5j,10j],[3+3j,1,4-8j],[1+1j,2j,-5+3j]])
        self.assertAlmostEqual(result,[[25.-10.j,-7. +0.j,0.+26.j],[-11.+11.j,-30.+15.j,-2. +0.j],[-35.-12.j,-24.+36.j,-1.+23.j]])

        result = lvm.prod_mat(a=[[2+8j,3j,-1+1j],[1j,0,-3j],[3-5j,-7,4+1j]],b=[[3j,-8j,3+10j],[9j,2,4-4j],[1j,2-6j,-1+1j]])
        self.assertAlmostEqual(result,[[-52. +5.j,68. -2.j,-62.+54.j],[0. +0.j,-10. -6.j,-7. +6.j],[14.-50.j,-40.-46.j,26.+46.j]])
    def test_accion(self):
        result = lvm.accion(m=[[-1,1+1j,0],[2-1j,0,1],[0,1-1j,1j]],v=[1,1+1j,1j])
        self.assertAlmostEqual(result,[-1.+2.j,2.+0.j,1.+0.j])

        result = lvm.accion(m=[[4+1j,-1],[2j,1j]],v=[1+1j,2-2j])
        self.assertAlmostEqual(result,[1.+7.j,0.+4.j])
    def test_prod_int(self):
        result = lvm.prod_int(x=[1,2+3j,6j],y=[0,1j,2+4j])
        self.assertAlmostEqual(result,(27-10j))

        result = lvm.prod_int(x=[4+2j,2j,6-1j],y=[10,5j,0])
        self.assertAlmostEqual(result,(50-20j))
    def test_norma(self):
        result = lvm.norma(v=[4+3j,6-4j,12-7j,13j])
        self.assertAlmostEqual(result, 20.952326839756964)

        result = lvm.norma(v=[5-7j,3+6j,1+13j])
        self.assertAlmostEqual(result, 17.0)
    def test_distancia(self):
        result = lvm.distancia(a=[2j,3,4j],b=[1j,-3,-5j])
        self.assertAlmostEqual(result, 10.862780491200215)

        result = lvm.distancia(a=[1-1j,3j,4],b=[0,-3j,2+6j])
        self.assertAlmostEqual(result, 8.831760866327848)
    def test_val_vect_prop(self):
        result = lvm.val_vect_prop(m=[[4j,-1],[2j,1]])
        self.assertAlmostEqual(result, """valores propios [-0.43084049+4.14859583j  1.43084049-0.14859583j] vectores propios [[ 0.90995455+0.j         -0.07244093-0.21003608j]
 [ 0.39204527-0.13521545j  0.97500623+0.j        ]]""")

        result = lvm.val_vect_prop(m=[[0,-1j],[3j,1+1j]])
        self.assertAlmostEqual(result, """valores propios [-1.23801342+0.35615761j  2.23801342+0.64384239j] vectores propios [[-0.16953064+0.58929304j -0.10908707-0.3791896j ]
 [ 0.78993232+0.j          0.91886629+0.j        ]]""")
if __name__ == '__main__':
    unittest.main()