emptyList = []

listElements = int(input("Please enter how many list elements you would like placed in order:"))

for i in range (1, listElements +1):
    value = int(input("Please enter the Value of %d Element:" %i))
    emptyList.append(value)
for i in range (listElements):
    for j in range (i+1, listElements):
        if(emptyList[i] > emptyList[j]):
            temp=emptyList[j]
            emptyList[i] = emptyList[j]
            emptyList[j] = temp
print ("Your List after sorting in Ascending Order is:", emptyList) 