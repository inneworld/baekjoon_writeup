n = int(input())
array = sorted([list(map(int, input().split())) for _ in range(n)] , key = lambda x: (x[1],x[0]))
cnt = key = 0

for i in range(n):
    if(array[i][0] >= key):
        key = array[i][1]
        cnt +=1

print(cnt)