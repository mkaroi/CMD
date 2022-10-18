def rec():
    lr = float(input('Enter the length of a Rectangle: '))
    br = float(input('Enter the breadth of a Rectangle: '))
    Area = lr * br
    print("Area of a Rectangle is: ",Area)
def tri():
    # Python Program to find the area of triangle

    a = float(input ("Please enter the length of side (1/3): ")) 
    b = float(input ("Please enter the length of side (2/3): ")) 
    c = float(input ("Please enter the length of side (3/3): ")) 

    # Uncomment below to take inputs from the user
    # a = float(input('Enter first side: '))
    # b = float(input('Enter second side: '))
    # c = float(input('Enter third side: '))

    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('The area of the triangle is %0.2f' %area)  
def cir():
    yummy_pie = 3.14  
    Radius = float(input ("Please enter the radius of the given circle: "))  
    area_of_the_circle = yummy_pie * Radius * Radius  
    print("The area of the given circle is: ", area_of_the_circle)  
def sqr():
    side = float(input("Enther the length of any side: "))
    Area = side*side
    print("Area of the square is: ", Area)