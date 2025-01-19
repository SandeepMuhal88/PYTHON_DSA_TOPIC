def Linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            print(f"Element found={target}")
            return
    print("Element not found")


l1=[52,85,96,10,8,9,65,2,1,63,48,963]
Linear_search(l1,963) # Element found at index 5