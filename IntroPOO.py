# Definición de una clase llamada 'Persona'
class Persona:
    # Atributos de clase (compartidos por todas las instancias)
    especie = 'Humano'  # Este es un atributo de clase

    # Constructor de la clase (el método especial __init__ se usa para inicializar las instancias)
    def __init__(self, nombre, edad):
        # Atributos de instancia (propios de cada objeto)
        self.nombre = nombre  # Este es un atributo de instancia
        self.edad = edad  # Este es otro atributo de instancia

    # Método de instancia (define el comportamiento de la clase)
    def saludar(self):
        return f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.'

    # Método de clase (afecta a toda la clase y no a una instancia en particular)
    @classmethod
    def especie_info(cls):
        return f'La especie es {cls.especie}.'

    # Método estático (no depende de la instancia ni de la clase)
    @staticmethod
    def mensaje_estatico():
        return 'Este es un mensaje estático, no depende de la clase ni de la instancia.'


# Crear una instancia de la clase 'Persona'
persona1 = Persona('Ana', 25)

# Usar los métodos e imprimir los atributos
print(persona1.saludar())  # Método de instancia
print(Persona.especie_info())  # Método de clase
print(Persona.mensaje_estatico())  # Método estático
print(f'Nombre: {persona1.nombre}, Edad: {persona1.edad}')  # Acceder a atributos de instancia
