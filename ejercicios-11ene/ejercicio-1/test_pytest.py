from contraseña import Usuario

def test_valida_contraseña():
    user = Usuario()
    assert user.valida_contraseña("abc.123") == False
    assert user.valida_contraseña("Abc.123") == False
    assert user.valida_contraseña("AbC.123") == True
    assert user.valida_contraseña("AbC.1 23") == False
    assert user.valida_contraseña("ÁbC.123") == False


"""
abc.123 es válida: False
Abc.123 es válida: False
AbC.123 es válida: True
AbC.1 23 es válida: False
ÁbC.123 es válida: False

"""