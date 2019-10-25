import random 

#bubble sort
#compares two values and swaps if the left is bigger than the right
def bubble_sort(array_list):
    print ("We will sort this list into order ", array_list)
    n = len(array_list)-1

    for j in range(n):
        for i in range(n): 
             if array_list[i] > array_list[i+1]:
                 array_list[i], array_list[i+1]=array_list[i+1], array_list[i]
                 i+=1
        n-=1
        
    print (array_list)

#This will create a new list of a random number of elements and random numbers
k=0
newlist=[]
arraylen=random.randrange(3,10)#random length of the array
while k<arraylen:
    newlist.append(random.randrange(0,10))#appends new values to the array
    k+=1


bubble_sort(newlist)
close=input('Enter anything to close')
