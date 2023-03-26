q = int(input("p :"))
w = int(input("k :"))
if q <= w:
  sum = 0
  for i in range(q, w + 1):
    print("All :", i, end="  ")
    if i % 7 == 0:
      print()
      print("---%7 :", i, end="  ")
      print()
    if i % 5 == 0:
      sum += 1
  print()
  print("----%5 :", sum)
  print()
  print("----Allspd :")
  for j in range(w, q - 1, -1):
    print(j, end="  ")
else:
  sum = 0
  for i in range(q, w - 1, -1):
    print("All :", i, end="  ")
    if i % 7 == 0:
      print()
      print("---%7 :", i, end="  ")
      print()
    if i % 5 == 0:
      sum += 1
  print()
  print("----%5 :", sum)
  print()
  print("----Allspd :")
  for j in range(w, q + 1):
    print(j, end="  ")
