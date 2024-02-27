class alive():
    pass
class animals():
    pass
class animals(alive):
    def eat(self):
        print('eating')
    def run(self):
        print('running')
    
class mammals(animals):
    def feed_kids(self):
        print('feeding_kids')
        
class lions(mammals):
    def eat_meat(self):
        print('eating meat')
        
Rex=lions()
Ron=lions()
Rex.run
Ron.eat_meat