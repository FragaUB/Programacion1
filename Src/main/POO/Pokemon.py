class DiccPokemon:
    def dic_pokemon():
        return {
            "Fuego": {
                'Electrico': 1/4,
                'Fuego': 1/4,
                'Agua': 1/2,
            },
            "Electrico": {
                'Electrico': 1/4,
                'Fuego': 1/4,
                'Agua': 0,
            },
            "Agua": {
                'Electrico': 1/2,
                'Fuego': 0,
                'Agua': 1/4,
            }
        }

class Pokemon:
    def __init__(self, nombre, saludmax, salud, tipo, tipo_ataque_a, tipo_ataque_b, sonido, Bool):
        self.nombre = nombre
        self.saludMax = saludmax
        self.salud = salud
        self.tipo = tipo
        self.tipo_ataque_a = tipo_ataque_a
        self.tipo_ataque_b = tipo_ataque_b
        self.sonido = sonido
        self.debilitado = Bool

    def __str__(self):
        return f"Nombre: {self.nombre}\nSalud Maxima: {self.saludMax}\nSalud Actual: {self.salud}\nTipo: {self.tipo}\nTipo Ataque A: {self.tipo_ataque_a}\nTipo Ataque B: {self.tipo_ataque_b}\nSonido: {self.sonido}\nDebilitado: {self.debilitado}"

    def emitirsonido(self):
        print(self.sonido)

    def atacar_a(self, otro_pokemon, valores_ataque):
        while self.salud > 0 and otro_pokemon.salud > 0:
            print(f"Che, {self.nombre} esta atacando a {otro_pokemon.nombre} con {self.tipo_ataque_a}")
            self.emitirsonido()
            valor_de_ataque = valores_ataque[self.tipo][otro_pokemon.tipo] 
            # Tomamos el valor de ataque segun el tipo de pokemon. Ejemplo: si es f vs a => self.tipo = Fuego, entra en dic = Fuego => otro_pokemon.tipo = agua => valor de ataque  = 1/2
            daño = 10 * valor_de_ataque
            otro_pokemon.salud -= daño
            print(f"{otro_pokemon.nombre} recibe {daño} de daño. Salud restante: {otro_pokemon.salud}")
            if otro_pokemon.salud <= 0:
                otro_pokemon.debilitado = True
                print(f"{otro_pokemon.nombre} ha sido debilitado.")
                break

            print(f"Che, {otro_pokemon.nombre} esta atacando a {self.nombre} con {otro_pokemon.tipo_ataque_a}")
            otro_pokemon.emitirsonido()
            valor_de_ataque = valores_ataque[otro_pokemon.tipo][self.tipo]
            daño = 10 * valor_de_ataque
            self.salud -= daño
            print(f"{self.nombre} recibe {daño} de daño. Salud restante: {self.salud}")
            if self.salud <= 0:
                self.debilitado = True
                print(f"{self.nombre} ha sido debilitado.")
                break

class PokemonElectrico(Pokemon):
    pass

class PokemonFuego(Pokemon):
    pass

class PokemonAgua(Pokemon):
    pass

class Main :
    def main():
        # Instanciacion de los pokemones :)
        valores_ataque = DiccPokemon.dic_pokemon()
        Pokemon1 = PokemonElectrico("Pikachu", 100, 100, "Electrico", "Impactrueno", "Rayo", "Pika Pika", False)
        print(Pokemon1)
        print("\n")
        Pokemon2 = PokemonFuego("Charmander", 100, 100, "Fuego", "Lanzallamas", "Ascuas", "Char Char", False)
        print(Pokemon2)
        print("\n")
        Pokemon3 = PokemonAgua("Squirtle", 100, 100, "Agua", "Pistola Agua", "Hidrobomba", "Squirtle Squirtle", False)
        print(Pokemon3)
        # Ataque entre Pikachu y Charmander
        result_ataque1 = Pokemon.atacar_a(Pokemon1, Pokemon2, valores_ataque)
        result_ataque2 = Pokemon.atacar_a(Pokemon3, Pokemon1, valores_ataque)
        print(f"\n{result_ataque1}\n")
        print(f"\n{result_ataque2}\n")

Main.main()

