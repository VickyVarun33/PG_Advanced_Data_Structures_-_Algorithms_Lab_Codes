a=[]
n= int(input("Enter the upper limit:"))
for i in range(n):
    w=int(input("enter the value:"))
    a.append(w)
x=int(input("enter the element you to search:"))
a=sorted(a)
print(x,a)
def binarys(number,array,low,high):
    if high<low:
        return -1
    mid=(low+high)//2
    if number==array[mid]:
        return mid
    elif number<=array[mid]:
        return binarys(x,a,low,mid-1)
    else:
        return binarys(x,a,mid+1,high)
def mysearch(x,a):
    return binarys(x,a,0,len(a)-1)
pos=mysearch(x,a)
if pos<0:
    print("Items not found")
else:
    print("Item found at the position:",pos+1)
    
    
