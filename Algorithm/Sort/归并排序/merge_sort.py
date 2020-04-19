def merge_sort(arr):
    sort(arr,0,len(arr)-1)

def sort(arr,low,high):
    if low<high:
        mid = (low + high)//2
        sort(arr,low,mid)
        sort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    contianer = []
    i, j = low, mid+1
    while i<=mid and j<=high:
        if arr[i]<arr[j]:
            contianer.append(arr[i])
            i += 1
        else:
            contianer.append(arr[j])
            j += 1
    if i<=mid:
        contianer.extend(arr[i:mid+1])
    elif j <= high:
        contianer.extend(arr[j:high+1])
    
    arr[low:high+1] = contiane
