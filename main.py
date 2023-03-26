mp = 0
mk = 100
p = k = -1
while p < mp or p > mk:
  p = int(input("p :"))
while k < mp or k > mk:
  k = int(input("k :"))
if p > k:
  p, k = k, p
for i in range(p, k + 1):
  if i % 2 != 0:
    print(i, end="  ")
