# Author CCG 9/29/21

score = input("How many points did your team score?")

if int(score) <= 8:
    print("Your team did not get a medal")
else:
    if int(score) <= 11:
        print("Your team got a bronze medal")
    else:
        if int(score) <= 14:
            print("Your team got a silver medal")
        else:
            print("Your team got a gold medal")
