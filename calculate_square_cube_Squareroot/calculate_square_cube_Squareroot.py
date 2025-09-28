class calculator():
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square is : {self.n*self.n}")
    def cube(self):
        print(f"cube is : {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"Squareroot is : {self.n**1/2}")


choice = input("Enter what you want to do Square Squareroot or cube of the number : ")
num = int(input("Enter any number : "))
st1 = calculator(num)


if(choice == "square"):
    st1.square()

elif(choice == "squareroot"):
    st1.squareroot()

elif(choice == "cube"):
    st1.cube()
