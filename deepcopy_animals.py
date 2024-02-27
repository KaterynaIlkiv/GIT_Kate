class Animal:
    def __init__(self,type,feed_quantity,color):
        self.type=type
        self.feed_quantity=feed_quantity
        self.color=color
        
import copy
harry= Animal('hipohryf',6,'pink')
kerry= Animal('spyder',8,'black')
billy= Animal('pony',4,'blue')
my_animals=[harry,kerry,billy]
more_animals=copy.deepcopy(my_animals)
my_animals[0].type='snake'
print(my_animals[0].type)
print(more_animals[0].type)