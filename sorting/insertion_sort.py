def insertion_sort(arr):
  for i in range(1,len(arr)):
    while arr[i]<=arr[i-1] and i!=0:
      temp=arr[i]
      arr[i]=arr[i-1]
      arr[i-1]=temp
      i=i-1
      print(arr)
  return arr

print(insertion_sort([12,4,2]))