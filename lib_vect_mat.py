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
###Continuación de la libreria
def daga(a):
    x = np.array(a)
    result = transp(conjug(x))
    return (result)
def prod_mat(a,b):
    if len(a[0]) == len(b[1]):
        x = np.array(a)
        y = np.array(b)
        result = np.matmul(x,y)
        return (result)
    else:
        return ("No cumple requerimientos") 
def accion(m,v):
    if len(m[0]) == len(v):
        mat = np.array(m)
        vect = np.array(v)
        result = np.array(np.dot(mat,vect))
        return (result)
    else:
        return ("No cumple requerimientos") 
def prod_int(x,y):
    if len(x) == len(y):
        v1 = daga(np.array(x))
        v2 = np.array(y)
        result = np.array(np.dot(v1,v2))
        return (result)
    else:
        return ("No cumple requerimientos") 
def norma(v):
    x = np.array(v)
    prod = prod_int(x,x)
    result = np.sqrt(prod)
    return (result.real)
def distancia(a,b):
    v1 = np.array(a)
    v2 = np.array(b)
    vr = v1 - v2
    result = norma(vr)
    return (result.real)
def val_vect_prop(m):
    if len(m) == len(m[0]):
        mat = np.array(m)
        valores,vectores = np.linalg.eig(m)
        return "valores propios {} vectores propios {}".format(valores, vectores)
    else:
        return ("No cumple requerimientos")
if __name__ == '__main__':
    print(add_vect([3+1j,4+4j,2j],[3+5j,2+2j,4j]))
    print("---------------------------------------")
    print(invad_vect([1+9j,2+5j,11-2j]))
    print("---------------------------------------")
    print(esc_vect(9,[-3+7j,1+6j,4-9j]))
    print("---------------------------------------")
    print(add_matr([[2+3j,5-5j,-4j],[6,5j,9+1j]],[[2-3j,-8+5j,10j],[3+3j,1,4-8j]]))
    print("---------------------------------------")
    print(invad_matr([[2+8j,6-6j,-12j],[7,9j,1+11j]]))
    print("---------------------------------------")
    print(esc_matr(9,[[3-2j,-2+5j,1j],[1+1j,2,3-1j]]))
    print("---------------------------------------")
    print(transp([[2+1j,2-2j,-6j],[2,3j,1+7j],[2-3j,-5+2j,9j]]))
    print("---------------------------------------")
    print(conjug([-4+2j,1-3j,2j]))
    ###Continuación
    print("---------------------------------------")
    print(daga([[2+8j,3j,-1+1j],[1j,0,-3j],[3-5j,-7,4+1j]]))
    print("---------------------------------------")
    print(prod_mat([[2+8j,3j,-1+1j],[1j,0,-3j],[3-5j,-7,4+1j]],[[3j,-8j,3+10j],[9j,2,4-4j],[1j,2-6j,-1+1j]]))
    print("---------------------------------------")
    print(accion([[4+1j,-1],[2j,1j]],[1+1j,2-2j]))
    print("---------------------------------------")
    print(prod_int([4+2j,2j,6-1j],[10,5j,0]))
    print("---------------------------------------")
    print(norma([5-7j,3+6j,1+13j]))
    print("---------------------------------------")
    print(distancia([1-1j,3j,4],[0,-3j,2+6j]))
    print("---------------------------------------")
    print(val_vect_prop([[0,-1j],[3j,1+1j]]))