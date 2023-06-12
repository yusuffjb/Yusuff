class Plane:
    def __init__(self):
        self.wings = 2

    def fly(self):
        print("The plane is flying.")


class Jet(Plane):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def fly(self):
        print("The jet is flying.")

    def display_color(self):
        print("Jet color:", self.color)


class Passenger(Plane):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def fly(self):
        print("The passenger plane is flying.")

    def display_color(self):
        print("Passenger plane color:", self.color)


# Creating objects
jet1 = Jet("White")
jet2 = Jet("Grey")
passenger1 = Passenger("Black")
passenger2 = Passenger("Orange")

#method overriding
jet1.fly()  
jet1.display_color()
#Inherited from Parent class
print("Jet wings:", jet1.wings)  

jet2.fly()
jet2.display_color()
print("Jet wings:", jet2.wings)

passenger1.fly()  
passenger1.display_color()  
print("Passenger plane wings:", passenger1.wings)

passenger2.fly()
passenger2.display_color()
print("Passenger plane wings:", passenger2.wings)
