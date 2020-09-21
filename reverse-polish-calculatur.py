import math
import operator
from collections import deque

class ReversePolishCalculator():

    def __init__(self):
        self.eingabe_liste = []
        self.stack = deque()
        self.operator_dict = { '+':operator.add,
                               '-':operator.sub,
                               '*':operator.mul,
                               '/':operator.truediv}


    def eingabe(self):
            eingabe = input('Rechenausdruck mit Leerzeichen: ')
            self.eingabe_liste = eingabe.split()
            print(f"Die Eingabe {self.eingabe_liste} wurde gespeichert.")
            print("Mit der Methode .calculate() kann gerechnet werden.")

    def number(self, elem):
            try:
                float(elem)
                return True
            except ValueError:
                pass

    def calculate(self, ausdruck=None):
        self.stack = deque()
        if ausdruck == None:
            ausdruck = self.eingabe_liste
        for elem in ausdruck:
            if self.number(elem):
                self.stack.append(float(elem))
            else:
                if len(self.stack) < 2:
                    print("Error: insufficient values in expression")
                    break
                else:
                    print("stack: %s" % self.stack)
                    if len(elem) == 1:
                        right = float(self.stack.pop())
                        left = float(self.stack.pop())
                        result = self.operator_dict[elem](left,right)
                        self.stack.append(float(result))
                    else:
                        left = float(self.stack.pop())
                        result = self.operator_dict[elem](math.radians(left))
                        self.stack.append(float(result))
        if len(self.stack) > 1:
            print("Error: Eingabe zu kurz, da ist nichts zu rechnen")
            print(f"Ending stack {self.stack}")
        else:
            return self.stack[0]

rechner = ReversePolishCalculator()
rechner.eingabe()
