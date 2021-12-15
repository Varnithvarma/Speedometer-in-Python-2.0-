Question = input("What do you want to find?\n")
if Question == "Speed":
    Speed_Type = input("Enter your unit?\n")
    D_1 = float(input("Enter Distance:\n"))
    T_1 = float(input("Enter Time:\n"))
    print("Hence,Speed is",D_1/T_1,Speed_Type)


elif Question == "Distance":
    Distance_Type = input("Enter unit?:\n")
    S_1 = float(input("Enter Speed: \n"))
    T_2 = float(input("Enter Time:\n"))
    print("Hence,Distance is",S_1*T_2,Distance_Type)

elif Question == "Time":
    Time_Type = input("Enter unit?\n")
    S_2 = float(input("Enter Speed:\n"))
    D_2 = float(input("Enter Distance:\n"))
    print("Hence, Time is",D_2/S_2,Time_Type)

else:
    print("Error Try Again ")


