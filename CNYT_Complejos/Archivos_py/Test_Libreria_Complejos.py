import Libreria_Complejos as c
import math

def test_suma():
    assert c.suma([3,2], [7,5]) == [10,7], 'Debe ser 10 + 7i'

def test_resta():
    assert c.resta([4,8], [3,1]) == [1,7], 'Debe ser 1 + 7i'

def test_producto():
    assert c.producto([4, 5], [-8, 3]) == [-47,-28], 'Debe ser -47 -28i'

def test_division():
    assert c.division([4, -3], [2, 5]) == [-7/29,-26/29], 'Debe ser (-7/29)+(-26/29)i'

def test_conjugado():
    assert c.conjugado([-2, 8]) == [-2, -8], 'Debe ser -2 -8i'

def test_modulo():
    assert c.modulo([3, 4]) == 5.0, 'Debe ser 5.0'

def test_imprimir1():
    assert c.imprimir1([-1, 5]) == '-1 + 5i', 'Debe ser -1 + 5i'

def test_cartesiana_polar():
    assert c.cartesiana_polar([2, 2]) == [math.sqrt(8), math.atan(1)], 'Debe ser 8^(1/2) + aTan(1)i'

def test_polar_cartesiana():
    assert c.polar_cartesiana([2, math.pi/4]) == [math.sqrt(2), round(math.sqrt(2),15)], 'Debe ser 2^(1/2) + 2^(1/2)i'

def test_imprimir_exp():
    assert c.imprimir_exp([2, math.pi]) == '2e^(i3.1416)', 'Debe ser 2^(1/2) + 2^(1/2)i'

def test_potencia_n():
    assert c.potencia_n([1, 1], 4) == [-4, 0], 'Debe ser -4 + 0i'

if __name__ == '__main__':
    test_suma()
    test_resta()
    test_producto()
    test_division()
    test_conjugado()
    test_modulo()
    test_imprimir1()
    test_cartesiana_polar()
    test_polar_cartesiana()
    test_imprimir_exp()
    test_potencia_n()
    print('Prueba exitosa')