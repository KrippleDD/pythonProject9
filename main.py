lst = list(map(int, input().split()))

x = int(input())

lst.append(x)

lst = sorted(lst, reverse = True)

a = []

for i in range(0, len(lst)):

 if lst[i] == x:

   a.append(i + 1)

print(max(a))
