def Binaray_search(Arr,target):
    low=0
    high=len(Arr)-1
    while low<=high:
        mid=(low+high)//2
        if Arr[mid]==target:
            print(f"Element found at index {mid}")
            return
        elif Arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    print("Element not found")

l1=[1,2,8,9,10,48,52,63,65,85,96,963]
l1.sort()
Binaray_search(l1,963) # Element found at index 11