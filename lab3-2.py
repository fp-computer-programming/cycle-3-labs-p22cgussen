# Author CCG 9/28/21

score = input("How many points did your team score?")

if int(score) <= 8:
    print("Your team did not get a medal")
elif int(score) <= 11:
    print("Your team got a bronze medal")
elif int(score) <= 14:
    print("Your team got a silver medal")
else:
    print("Your team got a gold medal")
