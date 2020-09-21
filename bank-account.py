class Account():
    # Ergänze hier deinen Code. Du darfst den Code aus b)
    # natürlich hierhin übernehmen.

    def __init__(self, start, pin):
        self.credits = start
        self.pin = pin

    def display(self):
        print(self.credits)

    def pay_in(self, money):
        self.credits += money

    def withdraw(self, money, pin):
        if pin == self.pin:
            if self.credits > money:
                self.credits -= money
            else:
                print("Du kannst nur " + str(self.credits) + "€ abheben!")
        else:
            print("Falsche PIN! Konto gesperrt!")

Kunde111 = Account(500, "1234")
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25, "1234")
Kunde111.display()
Kunde111.withdraw(600, "12345")
