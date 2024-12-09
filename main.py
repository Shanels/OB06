import random


class Hero:
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(self.attack_power // 2, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name}, нанося {damage} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"Игра началась! {self.player.name} против {self.computer.name}\n")

        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}\n")

            turn += 1

        if self.player.is_alive():
            print(f"Победил {self.player.name}! Поздравляем!")
        else:
            print(f"Победил {self.computer.name}! Попробуйте ещё раз.")


if __name__ == "__main__":
    game = Game()
    game.start()
