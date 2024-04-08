class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} наносит урон {self.attack_power}. У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        turn = 0  # 0 - ход игрока, 1 - ход компьютера
        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                self.player.attack(self.computer)
                turn = 1
            else:
                self.computer.attack(self.player)
                turn = 0
        self.declare_winner()

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    player_name = input("Введите имя игрока: ")
    game = Game(player_name)
    game.start()