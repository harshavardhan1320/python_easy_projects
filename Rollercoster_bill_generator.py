height=int(input("enter the height in cm "))
bill=100
if height>120:
    print("you can take a ride ")
    age=int(input("enter your age "))
    if age<12:
        print("child ticket is 20 ")
        bill+=20
    elif age>12 and age<18:
        print("youth ticket is 30")
        bill+=30
    else:
        print("adults ticket is 40")
        bill+=40
    photo=input("do u want a photo please enter Y or N")
    if photo=="Y"or "y":
        new_bill=bill+20
        print("your final amount is ",new_bill)  
    else:
        print("your final amount is ",bill)

else:
    print(" sorry! you can't take the ride ")
