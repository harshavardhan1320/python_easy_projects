height=float(input(print('ehter your height ')))
weight=int(input(print('enter your weight ')))
bmi=(weight/(height**2))
print("your bmi is ",round(bmi,2))
if bmi<18.5:
    print("ypu are under weight")
elif bmi>18.5 and bmi<25:
    print("you are normal")
elif bmi>25 and bmi<30:
    print("you are over weight")
elif bmi>30 and bmi<35:
    print("you are obese")
else:
    print("you are clinically obese")
