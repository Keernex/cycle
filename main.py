q = int(input("p :"))
w = int(input("k :"))
if q <= w:
  for i in range(q, w + 1):
    if i % 7 == 0:
      print(i, end="  ")
else:
  for i in range(q, w - 1, -1):
    if i % 7 == 0:
      print(i, end="  ")