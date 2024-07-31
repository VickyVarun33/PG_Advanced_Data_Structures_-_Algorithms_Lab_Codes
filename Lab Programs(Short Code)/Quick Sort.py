def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop()
        lesser,greater=[],[]
    for i in arr:
        if i<pivot:
            lesser.append(i)
        else:
            greater.append(i)
    return quick_sort(lesser)+[pivot]+quick_sort(greater)



arr=[]
n=int(input("Enter the upper limit:"))
for i in range(0,n):
    arr.append(int(input("Enter the element:")))
print("Unsorted Array:")
print(arr)
print("Sorted Array:")
print(quick_sort(arr))
