a,m=0,6
new=[]
arr=[]
for i in range(0,6):
    arr.append([int(m) for m in input().split()])
for i in range(4):
    for j in range(4):
        ele= arr[i][j] + arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1]+arr[i+2][j+2]
        new.append(ele)
print(max(new))
