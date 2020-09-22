'''
# Assignment Suggestions

### Part 1: Getting Started

One of the first things I always do when writing a script is start a main block. Inside of the main block, you'll be calling the function that is going to run your game. This puts you in the mindset of programming top down. It also makes it easy to test your code.

What are you going to call the function that runs your program? It should be a name that describes what it does. Other than that, you have free reign.

### Part 2: Set Up the Game

A simple way to store a tic-tac-toe board is with a list of three lists, each three elements long. You'll want to initialize the board to something in the beginning - I suggest that you have the coordinates of the board squares to begin with. This will make it easier for users to specify where they want to play.

It also makes sense to print this initial board. Since you'll probably want to print the board after any play is made, it would make sense to make a function that prints the board to the screen in a friendly way. Here's what I'm imagining the solution board to look like initially:

```
[(0, 0), (1, 0), (2, 0)]
[(0, 1), (1, 1), (2, 1)]
[(0, 2), (1, 2), (2, 2)]
```
'''

class TicTacToe():
# Klasse TicTacToe initialisiert ein
# player = int value 0 or 1
# turn = counts the number of rounds odd = p0, even = p1
# game_finished = bool to end the game (while loop)
# playground = 2 Layer filled with tuples

    def __init__(self):
        self.player = 0
        self.turn = 0
        self.game__finished = False
        self.playground = [[(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)]]

    def visualize_playground(self):
        print(self.playground[0])
        print(self.playground[1])
        print(self.playground[2])

    def choose_player(self):
        self.player = self.turn % 2 + 1 #Funktion wählt den Player 0 oder 1

    def input_move(self):
        row = int(input("Player {} choose the row. We need an int".format(self.player)))
        if row < 0 or row > 2:
            print("int between 0 and 2")
        else:
            line = int(input("Player {} choose the line. We need a to int".format(self.player)))
            if line < 0 or line > 2:
                print("int between 0 and 2")
            else:
                if self.player == 1:
                    self.playground[line][row] = "X"
                else:
                    self.playground[line][row] = "O"

    def check_status(self):
        # tillt?
        if self.turn >= 9:
            self.show_board()
            print("The Game ends in a tie.")
            self.game__finished = True
        # winner?
        elif (len(set(self.playground[0])) == 1
              or len(set(self.playground[1])) == 1
              or len(set(self.playground[2])) == 1
              or len(set([self.playground[0][0],self.playground[1][0],self.playground[2][0]])) == 1
              or len(set([self.playground[0][1],self.playground[1][1],self.playground[2][1]])) == 1
              or len(set([self.playground[0][2],self.playground[1][2],self.playground[2][2]])) == 1
              or len(set([self.playground[0][0],self.playground[1][1],self.playground[2][2]])) == 1
              or len(set([self.playground[0][2],self.playground[1][1],self.playground[2][0]])) == 1):
            self.visualize_playground()
            print(f"You {self.player} won!")
            self.game__finished = True

    def count(self):
        self.turn += 1
        self.player += 1
        if self.turn >=9:
            self.game__finished = True

    def play(self):
        while spiel.game__finished == False:
            spiel.visualize_playground()
            spiel.choose_player()
            spiel.input_move()
            spiel.check_status()
            spiel.count()

spiel = TicTacToe()
spiel.play()
