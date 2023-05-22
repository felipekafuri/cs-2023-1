class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        pass

    def correr(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

    def correr(self):
        return f"{self.nome} está correndo!"


class Cavalo(Animal):
    def emitir_som(self):
        return "Relincho"

    def correr(self):
        return f"{self.nome} está correndo!"


class Preguica(Animal):
    def emitir_som(self):
        return "Som de preguiça"

    def correr(self):
        return f"{self.nome} é uma preguiça e não consegue correr rápido."


class AnimalTeste:
    @staticmethod
    def testar_animais():
        dog = Cachorro("Bobby", 5)
        horse = Cavalo("Relâmpago", 8)
        sloth = Preguica("Preguiça", 2)

        animals = [dog, horse, sloth]

        for animal in animals:
            print(animal.emitir_som())
            print(animal.correr())


class Veterinario:
    @staticmethod
    def examinar(animal):
        print(f"Examinando {animal.nome}...")
        print(animal.emitir_som())


class Zoologico:
    def __init__(self):
        self.jaulas = []

    def adicionar_animal(self, animal):
        if len(self.jaulas) < 10:
            self.jaulas.append(animal)
        else:
            print("Zoológico está cheio.")

    def mostrar_animais(self):
        for animal in self.jaulas:
            print(animal.emitir_som())
            print(animal.correr())


if __name__ == "__main__":
    zoo = Zoologico()

    dog = Cachorro("Bobby", 5)
    horse = Cavalo("Relâmpago", 8)
    sloth = Preguica("Preguiça", 2)

    zoo.adicionar_animal(dog)
    zoo.adicionar_animal(horse)
    zoo.adicionar_animal(sloth)

    zoo.mostrar_animais()

    vet = Veterinario()
    vet.examinar(dog)
    vet.examinar(horse)
    vet.examinar(sloth)

    AnimalTeste.testar_animais()
