class Persona:

    def __init__(self, apellidoPaterno, apellidoMaterno, nombre, ci, edad, sexo):
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.nombre = nombre
        self.ci = ci
        self.edad = edad
        self.sexo = sexo

    def compareTo(self, persona):

        if self.apellidoPaterno > persona.apellidoPaterno:
            return 1           
        if self.apellidoPaterno < persona.apellidoPaterno:
            return -1

        if self.apellidoMaterno > persona.apellidoMaterno:
            return 1
        if self.apellidoMaterno < persona.apellidoMaterno:
            return -1

        if self.nombre > persona.nombre:
            return 1
        if self.nombre < persona.nombre:
            return -1

        if self.ci > persona.ci:
            return 1
        if self.ci < persona.ci:
            return -1

        if self.edad > persona.edad:
            return 1
        if self.edad < persona.edad:
            return -1

        if self.sexo > persona.sexo:
            return 1
        if self.sexo < persona.sexo:
            return -1

        return 0




