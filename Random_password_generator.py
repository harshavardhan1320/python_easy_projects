import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
numbers=["1","2",'3','4','5','6','7','8','9']
symbols=["!","@",'#','$','%','^','&','*',';']

print("welcome to random passwoard generator ")
nr_letters=int(input("how many letters you would like to add in your passwoard"))
nr_symbols=int(input("how many symbols u would like to add"))
nr_numbers=int(input("how many numbers you would like to add"))

password=[]
for char in range (0,nr_letters):
    r=random.choices(letters)
    password+=r
for char in range (0,nr_symbols):
    r=random.choices(symbols)
    password+=r
for char in range (0,nr_numbers):
    r=random.choices(numbers)
    password+=r
random.shuffle(password)

passwoard_1=""
for char in password:
    passwoard_1+=char
print(passwoard_1)
