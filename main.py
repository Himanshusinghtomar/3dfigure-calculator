num1 = int(input(" Enter 1st number :-  "))
num2 = int(input(" Enter 2nd number :-  "))
opt = int(input(" Enter what you want to do \n 1 : Addition \n 2 : Sub \n 3 : multi \n 4 : Div \n :- "))
if opt == 1:
    print("Addition :-",num1 + num2)
elif opt == 2:
    print("Substraction :- ", num1-num2)gr
elif opt == 3:
    print("Multiplication :- ", num1 * num2)
elif opt == 4:
    print("Division :- ", num1 // num2)
else:
    print(" Sorry Wrong Input")