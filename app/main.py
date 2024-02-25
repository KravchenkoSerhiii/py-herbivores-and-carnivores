class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> str:
        return f"{self.name}: {self.health}"

    @staticmethod
    def remove_dead() -> None:
        Animal.alive = [animal for animal in Animal.alive if animal.health > 0]

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other_animals: Herbivore) -> None:
        if isinstance(other_animals, Herbivore) and not other_animals.hidden:
            other_animals.health -= 50
            if other_animals.health <= 0:
                Animal.alive.remove(other_animals)
