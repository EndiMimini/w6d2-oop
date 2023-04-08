class Parent:
    def buyBeer(self):
        print("Here you go! Enjoy it!")

class Child(Parent):
    def buyBeer(self):
        print("Hey, you are not 18 yet! Try again some years later!")

# dad = Parent()
# son = Child()
# dad.buyBeer()
# son.buyBeer() #notice this overrides the Parent method!

favorite_color = input('What is your favorite color? ') # input takes a prompt, which needs to be a string
print(f'Your favorite color is: {favorite_color}') 