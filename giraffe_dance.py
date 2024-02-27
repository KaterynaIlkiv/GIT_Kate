class giraffe:
    def left_leg_forward(self):
        print('Left leg forward')
    def left_leg_back(self):
        print('Left leg back')
    def right_leg_forward(self):
        print('Right leg forward')
    def right_leg_back(self):
        print('Right leg back') 
    def dance(self):
        self.left_leg_forward()
        self.left_leg_back()
        self.right_leg_forward()
        self.right_leg_back()
redg=giraffe()
redg.dance()