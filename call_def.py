class alive:
    pass
class animals(alive):
    pass
def breath(self):
       print('breathing')
def move(self):
       print('moving')
def eat_food(self):
       print('eating')
class mammals(animals):
    pass
class giraffe(mammals):
    pass
Rex=giraffe()
Ron=giraffe()
Rex.move()

class giraffe(mammals):
    def find_food(self):
        self.move()
        print('I found food')
        self.eat_food()
    def eat_leaves(self):
        self.eat.food()
    def dance(self):
        self.move()
        self.move()
        self.move()
        
Rex=giraffe()
Rex.move()

