"""
i. Longitud entre 6 y 20 caracteres.
ii. Debe contener al menos un número.
iii. Debe contener al menos dos mayúsculas.
iv. Debe contener al menos un carácter especial.
v. No puede contener espacios.
"""

import re

class Usuario:
    def __init__(self):
        self.usuario = None
        self.contraseña = None
    
    def set_usuario(self,usuario):
        self.usuario = usuario

    def set_contraseña(self,contraseña):
        valida_pass = self.valida_contraseña(contraseña)
        if valida_pass:
            self.contraseña=contraseña
            print("Se ha actualizado su contraseña correctamente!")
        else:
            print("La contraseña ingresada no cumple con los requisitos")

    def get_usuario(self):
        return self.usuario
    
    def get_contraseña(self):
        return self.contraseña
    
    def valida_contraseña(self,contraseña):
        if not (6 <= len(contraseña.replace(' ','')) <=20):
        #if not (len(contraseña.trim()) >= 6 and len(contraseña.trim()) <= 20):
            return False

        any_number_regex = "[0-9]"
        if not re.search(any_number_regex,contraseña):
            return False

        any_capital_letter = ".*([A-Z]).*([A-Z]).*"
        if not re.search(any_capital_letter,contraseña):
            return False

        special_ch_regex = "[$&+,:;=?@#|<>.^*()%!-]"
        if not re.search(special_ch_regex,contraseña):
            return False

        blank_space_regex = "[\s]"
        if re.search(blank_space_regex,contraseña):
            return False

        return True



user1 = Usuario()
user1.set_usuario("tati")
user1.set_contraseña("hR-ola98A")