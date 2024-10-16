import aritmetica

def test_sumar():
    assert aritmetica.sumar(5, 3) == 8
    assert aritmetica.sumar(-1, 1) == 0
    assert aritmetica.sumar(0, 0) == 0
    
def test_restar(): 
    assert aritmetica.restar(5, 3) == 2
    assert aritmetica.restar(-1, 1) == -2
    assert aritmetica.restar(0, 0) == 0
    
    
def test_dividir():
    assert aritmetica.dividir(10, 2) == 5
    assert aritmetica.dividir(-10, 2) == -5
    assert aritmetica.dividir(0, 2) == 0
    try:
        aritmetica.dividir(10, 0)
    except ValueError:
        pass
    else:
        assert False, "No se capturó la excepción correctamente"
        
def test_multiplicar():
    assert aritmetica.multiplicar(5, 3) == 15
    assert aritmetica.multiplicar(-1, 1) == -1
    assert aritmetica.multiplicar(0, 0) == 0
    
def test_sumar_n():
    assert aritmetica.sumar_n(5, 5, 5, 5) == 20
    assert aritmetica.sumar_n(-1, -1, -1, -1) == -4
    assert aritmetica.sumar_n(0, 0, 0, 0) == 0
    
def test_promedio_n():
    assert aritmetica.promedio_n(5, 5, 5, 5) == 5
    assert aritmetica.promedio_n(-1, -1, -1, -1) == -1
    assert aritmetica.promedio_n(0, 0, 0, 0) == 0
    
    
if _name_ == '_main_':
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Todos los test pasaron correctamente")
