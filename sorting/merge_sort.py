def merge(a,b):
  arr = []
  i=0
  j=0
  while(i!=len(a) or j!=len(b)):
    if i==len(a):
      arr = arr+b[j:]
      j=len(b)
    elif j==len(b):
      arr = arr+a[i:]
      i=len(a)
    elif a[i]>b[j]:
      arr.append(b[j])
      j=j+1
    elif b[j]>a[i]:
      arr.append(a[i])
      i=i+1
    elif a[i]==b[j]:
      arr.append(a[i])
      arr.append(a[i])
      i=i+1;
      j=j+1;
  return arr;

def sort(arr):
  if(len(arr)==1):
    return arr
  n = int(len(arr)/2)
  a=sort(arr[:n])
  b=sort(arr[n:])
  return(merge(a,b))

print(sort([12,4,7,39,96,2,12,45]))