print("welcome to pizza deliveries :)")
size=input("Please enter the size of pizza you would like to have s,m,l ")
if size=="s" :
    print("price of small pizza is 150 RS")
    price=150
elif size=="m" :
    print("price of medium pizza is 200 RS")
    price=200
else :
    print("price of large pizza is 250 RS")
    price=250
pepperoni=input("would u like to add peproni y or n")
if pepperoni=="y":
    print("cost of pepperioni is 40")
    new_price=price+40
cheese=input("would u like to add extra cheese y or n")
if cheese=="y":
    print("cost of cheese is 50")
    new_price+=50

print("your total bill amount is",new_price)