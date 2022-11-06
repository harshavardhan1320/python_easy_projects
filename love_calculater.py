print("welcome to love calculater")
N1=input("enter your name ")
N2=input("enter your crush name")
n1=N1.lower()
n2=N2.lower()

t1=n1.count("t")
t2=n2.count("t")
t=t1+t2
r1=n1.count("r")
r2=n2.count("r")
r=r1+r2
u1=n1.count("u")
u2=n2.count("u")
u=u1+u2
e1=n1.count("e")
e2=n2.count("e")
e=e1+e2
total1=t+r+u+e


l1=n1.count("l")
l2=n2.count("l")
l=l1+l2
o1=n1.count("o")
o2=n2.count("o")
o=o1+o2
v1=n1.count("v")
v2=n2.count("v")
v=v1+v2
total2=l+o+v+e

total=str(total1) +str(total2)
print(f"your love score is {total} ")