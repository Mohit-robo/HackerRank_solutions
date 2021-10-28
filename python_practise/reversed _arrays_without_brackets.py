n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
# rev = arr.reverse()
for i in range(len(arr)-1, -1, -1):     
  print(arr[i],end=" ")
