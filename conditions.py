print("Rules that govern the state of water")

# user picks temp, see what happens to the state of water
# cutternt_temp is the temp variable
current_temp = False

# Enter Temp Value
while current_temp is False:
    current_temp = input ("Enter a temperature: \n")
    print(current_temp)

#IF statement, solid
    if (int(current_temp) < 0) or (int(current_temp) == 0):
        print("water is a solid. Ice.")
        current_temp = False

# IF statement, liquid
    elif (int(current_temp) < 100):
        print("Still a liquid!")
        current_temp = False

# if statment, vapour
    elif(int(current_temp) > 100) or (int(current_temp) == 100):
        print("Vape Naysh")
        current_temp = False
