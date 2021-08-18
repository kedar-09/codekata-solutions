list=[]
num=int(input("Enter number of balls to be added: "))

for i in range(0, num):
    elements=int(input())
    list.append(elements)

print("Rack:", list)
leng=len(list)
print("Number of balls: ",leng)

#Bubble sort. Outer loop is used for looping the elements till the end and the inner loop is used for comparing elements
for i in range(leng-1):
    for j in range(leng-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print("Sorted rack: ",list)
