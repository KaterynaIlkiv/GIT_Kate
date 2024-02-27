class Animal:
    def __init__(self,type,feed_quantity,color):
        self.type=type
        self.feed_quantity=feed_quantity
        self.color=color
    
import copy
harry= Animal('hipohryf',6,'pink')
harryet=copy.copy(harry)
print(harry.type)
print(harryet.type)