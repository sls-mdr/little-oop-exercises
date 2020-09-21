class Cube():

    def __init__(self, side):
        self.side = side

    def surface(self):
        print(self.side ** 2 * 6)

    def volume(self):
        print(self.side ** 3)


#create instanz
a = Cube(3)

#test functions
a.surface()
a.volume()
