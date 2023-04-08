class Coffee:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200

    def make_coffee(self,numberOf):
        print('Making', numberOf, 'coffees')
        print("Coffees are done")
        return self

    def clean(self):
        print("Cleaning the coffe esspresso!")
        return self

class Cappuccino( Coffee ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"

    def make_cappuccino(self,numberOf):
        super().make_coffee(numberOf) ## its using the make_coffe method, which basically makes coffe
        print("Adding milk to become cappucinos!!!")
        print("Cappucinos are done! Enjoy")
        return self
    #Polymorphisms or overriding
    def clean(self):
        print("Cleaning the cappucino espresso!")
        return self
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = Coffee("Cafe")
        #abstraction
    def make_coffe(self, numberOf):
        self.cafe.make_coffee(numberOf)

barista = Barista('Endi')
barista.make_coffe(3)


# order1 = Cappuccino("Table 1")
# order1.make_cappuccino(3)
# order1.clean()