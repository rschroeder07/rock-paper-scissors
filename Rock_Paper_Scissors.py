import random

moves = ['rock', 'paper', 'scissors']


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            HumanPlayerMove = input("rock, paper, or scissors?\n").lower()
            if HumanPlayerMove in moves:
                return HumanPlayerMove
            print("Invalid move, play rock, paper, or scissors")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    player_one_score = 0
    player_two_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.player_one_score += 1
            print("Player 1 Wins!")
            print(f"Player 1 Score: {self.player_one_score}\t "
                  f"Player 2 Score: {self.player_two_score}")
        elif beats(move2, move1):
            self.player_two_score += 1
            print("Player 2 Wins!")
            print(f"Player 1 Score: {self.player_one_score}\t "
                  f"Player 2 Score: {self.player_two_score}")
        else:
            print("It's a tie!")
            print(f"Player 1 Score: {self.player_one_score}\t "
                  f"Player 2 Score: {self.player_two_score}")

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"\u001b[30m\u001b[43m Round {round +1}:\u001b[0m")
            self.play_round()
        if self.player_one_score > self.player_two_score:
            print("\n\u001b[33m\u001b[44m Congrats, you won! \u001b[0m")
        elif self.player_one_score < self.player_two_score:
            print("\n\u001b[31m\u001b[40m Sorry, you lost... \u001b[0m")
        elif self.player_one_score == self.player_two_score:
            print("\n\u001b[37m\u001b[45m It's a tie! \u001b[0m")
        print("\n\u001b[30m\u001b[47m Game over. \u001b[0m")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
