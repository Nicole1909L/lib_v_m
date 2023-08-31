import numpy as np
def add_vect(v1,v2):
    vect1 = np.array(v1)
    vect2 = np.array(v2)
    result = vect1 + vect2
    return (result)
def invad_vect(v):
    vect = np.array(v)
    result = vect * (-1)
    return (result)
def esc_vect(e,v):
    vect = np.array(v)
    result = e * vect
    return (result)
def add_matr(m1,m2):
    mat1 = np.array(m1)
    mat2 = np.array(m2)
    result = mat1 + mat2
    return (result)
def invad_matr(m):
    mat = np.array(m)
    result = mat * (-1)
    return (result)
def esc_matr(e,m):
    mat = np.array(m)
    result = e * mat
    return (result)
def transp(a):
    x = np.array(a)
    result = np.transpose(x)
    return (result)
def conjug(a):
    x = np.array(a)
    result = x.conjugate()
    return (result)
if __name__ == '__main__':
    print(add_vect([3+1j,4+4j,2j],[3+5j,2+2j,4j]))
    print(invad_vect([1+9j,2+5j,11-2j]))
    print(esc_vect(9,[-3+7j,1+6j,4-9j]))
    print(add_matr([[2+3j,5-5j,-4j],[6,5j,9+1j]],[[2-3j,-8+5j,10j],[3+3j,1,4-8j]]))
    print(invad_matr([[2+8j,6-6j,-12j],[7,9j,1+11j]]))
    print(esc_matr(9,[[3-2j,-2+5j,1j],[1+1j,2,3-1j]]))
    print(transp([[2+1j,2-2j,-6j],[2,3j,1+7j],[2-3j,-5+2j,9j]]))
    print(conjug([-4+2j,1-3j,2j]))

