print("Act 9 clase humano")
print("David Yair Matínez Nava 22308051281077")

# zona de clase

class Humano1077:
    #zona de atributos dentro de la clase
    edad = 17
    genero = "mujer"
    color_piel = "blanco"
    telefono = "676-6758-443"
    direccion = "Av. Dolores"


    #zona de funciones dentro de la clase
    def correr1077(self, nombre):
        print(f"{nombre} está corriendo ufff")

    def saltar1077(self, nombre):
        print(f"{nombre} está saltando ")

    def mirar1077(self, nombre):
        print(f"{nombre} está mirando")
    
    def cantar1077(self, nombre):
        print(f"{nombre} está cantando")

    def escribir1077(self, nombre):
        print(f"{nombre} está escribiendo")


    def bailar1077(self, nombre):
        print(f"está bailando: {nombre}")

    def ejercitar1077(self,nombre):
        print(f"se está ejercitando: {nombre}")
    

# zona de creacion de objetos
david = Humano1077()
loid = Humano1077()

# zona de usando objetos

print("--Resultados para David--")
david.edad = 13
david.genero = "hombre"
david.color_piel = "negra"
david.telefono = "657- 757- 3456"
print(f"Edad: {david.edad}") 
print(f"genero: {david.genero}")
print(f"color de piel: {david.color_piel}")
print(f"telefono: {david.telefono}")
print("\nmetodos david")
david.correr1077("David")
david.saltar1077("David")
david.mirar1077("David")
david.cantar1077("David")




print("\n--Resultado para Loid--")
loid.edad = 13
loid.genero = "mujer"
loid.color_piel = "negra"
loid.telefono = "656-676- 5678"
loid.direccion = "Av_colores"

print(f"Edad: {loid.edad}") 
print(f"genero: {loid.genero}")
print(f"color de piel: {loid.color_piel}")
print(f"telefono: {loid.telefono}")
print(f"direccion: {loid.direccion}")

print("\nmetodos Loid")
loid.correr1077("loid")
loid.saltar1077("loid")
loid.mirar1077("loid")




