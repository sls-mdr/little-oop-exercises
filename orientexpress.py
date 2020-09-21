class Train():
    #Ein Zug fährt durch Europa.

    def __init__(self, route, start):
        self.route = route
        self.position = start

    def show_station(self):
        print(self.route[self.position])

    def move(self):
        if self.position < len(self.route) - 1:
            self.position += 1
        else:
            print("Endstation! Alle aussteigen!")

    def move_back(self):
         if self.position > 0:
            self.position -= 1

    def bypass_station(self, station):
        if station in self.route:
            self.route.remove(station)
            self.position = 0


orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.move_back()
orientexpress.show_station()
orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.bypass_station("Budapest")
orientexpress.move()
orientexpress.show_station()
