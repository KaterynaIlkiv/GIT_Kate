class mammals:
    pass
class giraffe(mammals):
    def find_food(self):
        self.move()
        print('I found food')
        self.eat_food()
    def eat_leaves(self):
        self.eat_food()
    def dance(self):
        self.move()
        self.move()
        
        redg = giraffe()
        redg.dance()