# Atributos de clase

# Definimos la clase coche
class Coche:
    ruedas = 4  # Atributo de clase: Todas las instancias de coche tienen 4 ruedas

    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia


# Imprimir el atributo de clase
print(Coche.ruedas)

# Crear instancias de la clase Coche
coche1 = Coche('Toyota', 'Corolla')
coche2 = Coche('Honda', 'Civic')

# Acceder al atributo de clase de las instancias
print(coche1.ruedas)
print(coche2.ruedas)

# En la clase coche, el atributo ruedas es un atributo de clase que se aplica
# a todas las instancias de la clase, estableciendo que cada coche tiene 4 ruedasç
# Este atributo se puede acceder tanto desde la clase como desde las instancias
# permite compartir datos comunes entre todos los objetos de esa clase
