def mergeSort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2 

    left=arr[:mid]
    right=arr[mid:]

    left=mergeSort(left)
    right=mergeSort(right)

    return merge(left,right)


def merge(left,right):
    merged=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    merged.extend(left[i:])
    merged.extend(right[j:])


    return merged


a1=[7,4,9,11,1,3,22]


result=mergeSort(a1)

print(result)
