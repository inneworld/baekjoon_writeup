n = int(input())
array = sorted(list(map(int,input().split())) , key = lambda x :x)
array2 = sorted(list(map(int,input().split())), key = lambda x : -x)
sum = 0
for i in range(n):
    sum += (array[i] * array2[i])

print(sum)
