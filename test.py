class MyAppValueError(ValueError):
    def __init__(self, message, *args):
        super(MyAppValueError, self).__init__(message, *args)


class Persona:
    def setEdad(self, edad):
        if (edad <= 0):
            raise MyAppValueError("La edad debe ser positiva.")
        self.edad = edad


try:
    persona = Persona()
    persona.setEdad(-10)
except MyAppValueError as e:
    print(e)
