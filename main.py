# 3d Figure Calculator
def cuboid():
    x = int(input("What you want \n 1:Volume \n 2:TSA \n 3:LSA \n  :-"))
    if x == 1:
        print("You selected Volume")
        length = eval(input("Enter length of cuboid :- "))
        breadth = eval(input("Enter breadth of cuboid :- "))
        height = eval(input("Enter height of cuboid :- "))
        print("volume is :-", length * breadth * height)
    elif x == 2:
        print("You selected Total Surface area")
        length = eval(input("Enter length of cuboid :- "))
        breadth = eval(input("Enter breadth of cuboid :- "))
        height = eval(input("Enter height of cuboid :- "))
        print("T*S*A is :-", 2 * (length * breadth + breadth * height + length * height))
    elif x == 3:
        print("You selected Lateral surface area ")
        length = eval(input("Enter length of cuboid :- "))
        breadth = eval(input("Enter breadth of cuboid :- "))
        height = eval(input("Enter height of cuboid :- "))
        print("L*S*A is :-", 2 * height * (length + breadth))
    else:
        print(" Diagonal & Perimeter are coming soon ")


def cube():
    i = int(input("What you want \n 1:Volume \n 2:TSA \n 3:LSA \n  :-"))
    if i == 1:
        print("You selected Volume")
        side = eval(input("Enter length of cube :- "))
        print("Volume is :-", side * side * side)
    elif i == 2:
        print(" You selected Total Surface area ")
        side = eval(input("Enter length of cube :- "))
        print("T*S*A is :-", 6 * (side * side))
    elif i == 3:
        print(" You selected Lateral Surface area ")
        side = eval(input("Enter length of cube :- "))
        print(" L*S*A is :- ", 4 * (side * side))
    else:
        print(" Diagonal & Perimeter are coming soon ")


def cylinder():
    j = int(input("What you want \n 1:Normal Cylinder \n 2:HOLLOW Cylinder \n  :-"))
    if j == 1:
        i = int(input("What you want \n 1:Volume \n 2:TSA \n 3:CSA \n  :-"))
        if i == 1:
            print("You selected Volume")
            radius = eval(input("Enter radius of cylinder :- "))
            height = eval(input("Enter height of cylinder :- "))
            print("Volume is :-", (3.14 * radius * radius * height))
        elif i == 2:
            print(" You selected Total Surface area ")
            radius = eval(input("Enter radius of cylinder :- "))
            height = eval(input("Enter height of cylinder :- "))
            print("C*S*A is :-", (2 * 3.14 * radius * (radius + height)))
        elif i == 3:
            print("You selected Curve Surface Area")
            radius = eval(input("Enter radius of cylinder :- "))
            height = eval(input("Enter height of cylinder :- "))
            print("C*S*A is :-", (2 * 3.14 * radius * height))
        else:
            print("wrong Input")
    elif j == 2:
        i = int(input("What you want \n 1:Volume \n 2:CSA \n  :-"))
        if i == 1:
            print('You selected Volume of Hollow Cylinder')
            radius1 = eval(input("Enter  external radius  of cylinder :- "))
            radius2 = eval(input("Enter  enteral radius  of cylinder :- "))
            height = eval(input("Enter height of cylinder :- "))
            print("Volume is :-", 3.14 * height * (radius1 * radius1 - radius2 * radius2))
        elif i == 2:
            print('You selected C*S*A of Hollow Cylinder')
            radius1 = eval(input("Enter  external radius  of cylinder :- "))
            radius2 = eval(input("Enter  enteral radius  of cylinder :- "))
            height = eval(input("Enter height of cylinder :- "))
            print("C*S*A is :-", 2 * (3.14 * height * radius1) + 2 * (3.14 * height * radius2))
    else:
        print(" Wrong Input")


def sphere():
    i = int(input("What you want \n 1:Volume \n 2:TSA \n  :-"))
    if i == 1:
        print(" You Selected Volume of sphere ")
        radius = eval(input(" Enter the radius of Sphere :- "))
        print("Volume of a sphere :- ", (4 / 3 * 3.14 * radius * radius * radius))
    elif i == 2:
        print(" You Selected T*S*A of sphere ")
        radius = eval(input(" Enter the radius of Sphere :- "))
        print("T*S*A of a sphere :- ", (4 / 3 * 3.14 * radius * radius))
    else:
        print(" Wrong Input ")


def hemisphere():
    i = int(input("What you want \n 1:Volume \n 2:TSA \n 3:CSA \n  :-"))
    if i == 1:
        print(" You Selected Volume of hemisphere ")
        radius = eval(input(" Enter the radius of hemisphere :- "))
        print("Volume of a hemisphere :- ", (2 / 3 * 3.14 * radius * radius * radius))
    elif i == 2:
        print(" You Selected T*S*A of hemisphere ")
        radius = eval(input(" Enter the radius of hemisphere :- "))
        print("T*S*A of a hemisphere :- ", (3 * 3.14 * radius * radius))
    elif i == 3:
        print(" You Selected C*S*A of hemisphere ")
        radius = eval(input(" Enter the radius of hemisphere :- "))
        print("C*S*A of a hemisphere :- ", (2 * 3.14 * radius * radius))

    else:
        print(" Wrong Input ")


def cone():
    i = int(input("What you want \n 1:Volume \n 2:TSA \n 3:CSA \n  :-"))
    if i == 1:
        print(" You Selected Volume of cone ")
        radius = eval(input(" Enter the radius of cone :- "))
        height = eval(input("Enter height of cone :- "))
        print("Volume of a cone :- ", (1 / 3 * 3.14 * radius * radius * height))
    elif i == 2:
        print(" You Selected T*S*A of cone ")
        radius = eval(input(" Enter the radius of cone :- "))
        length = eval(input("Enter length of cone :- "))
        print("T*S*A of a cone :- ", (3.14 * radius * length))
    elif i == 3:
        print(" You Selected C*S*A of cone ")
        radius = eval(input(" Enter the radius of cone :- "))
        length = eval(input("Enter length of cone :- "))
        print("T*S*A of a cone :- ", (3.14 * radius * (radius + length)))

    else:
        print(" Wrong Input ")


run = True
while run == True:
        print(" 3d Figure Calculator ")
        w = int(input(" Select the 3D \n 1:Cuboid \n 2:Cube \n 3:Cylinder \n 4:Sphere \n 5:Hemisphere \n 6:Cone \n :- "))
        if w == 1:
            cuboid()
        elif w == 2:
            cube()
        elif w == 3:
            cylinder()
        elif w == 4:
            sphere()
        elif w == 5:
            hemisphere()
        elif w == 6:
            cone()

        else:
            print(" Wrong input ")
        i = input("Enter Y for continue and N for stop :- ").upper()
        if i == "Y":
            run = True
        elif i == "N":
            run = False
        else:
            print("worng input ")
