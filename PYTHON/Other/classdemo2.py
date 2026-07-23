class phone():
    def set_color(self,color):
        self.color=color
    
    def set_cost(self,cost):
        self.cost=cost

    def show_color(self):
        return self.color
    
    def show_cost(self):
        return self.cost
    
    def make_call(self):
        print("Make a call")
    
    def play_gama(self):
        print("Play Game")

p1=phone()
p2=phone()

p1.set_color("black")
p1.set_cost(35000)

color=p1.show_color()
cost=p1.show_cost()

print("Color=",color)
print("Cost=",cost)

p2.set_color("Blue")
p2.set_cost(40000)

color=p2.show_color()
cost=p2.show_cost()

print("Color=",color)
print("Cost=",cost)