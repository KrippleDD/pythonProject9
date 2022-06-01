lst = list(map(int, input().split()))

x = int(input())

lst.append(x)

lst = sorted(lst, reverse = True)

a = [5, 8, 2, 8, 4, 7, 0, 3, 1, 6, 9]

for i in range(0, len(lst)):

 if lst[i] == x:

   a.append(i + 1)

print(max(a))
