array_list=[]
k=0
answer=int(input("how big is the list?"))

while k<answer:
    array_list.append(int(input("enter val")))#adds the number onto the list, converts it to int before storing
    k+=1


print("Unsorted list pre-insertion sort: ",array_list)#prints out the array 


#for loop enables the sort to repeat
for i in range(len(array_list)-1):#goes through the range of the list -1
    j=i #j is made the same as i
    while j>=0:#whilst j is more than -1
        if array_list[j]>array_list[j+1]:#compares the two items
            array_list[j],array_list[j+1]=array_list[j+1],array_list[j] #swap if in wrong order
        j-=1 #j decreases and while loop repeats
        #while loop repeats until it is -1 therefore out of range of list

print (array_list)

