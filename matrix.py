row1=["#","#","#"]
row2=["#","#","#"]
row3=["#","#","#"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("where do u want to put the treasure ")
a=int(position[0])
b=int(position[1])
b1=(map[b-1])
b1[a-1]="X"
print(f"{row1}\n{row2}\n{row3}")
