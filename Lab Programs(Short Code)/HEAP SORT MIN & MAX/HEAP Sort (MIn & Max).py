def heapify(arr,n,i):
    largest=i
    left_child=2*i+1
    right_child=2*i+2
    if left_child<n and arr[left_child]>arr[largest]:
       largest=left_child
    if right_child<n and arr[right_child]>arr[largest]:
        largest=right_child
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heap_sort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
arr=[]
n=int(input("Enter the size of an Array: "))
for i in range(1,n+1):
    arr.append(int(input(f"enter Number {i} : ")))
heap_sort(arr)
rev=list(reversed(arr))
print("Sorted array using max heap:",rev)
print("Sorted array using min heap:",arr)


