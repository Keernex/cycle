deagin = int(input("deagin :"))
end = int(input("end :"))
if end > deagin:
  for i in range(end, deagin - 1, -1):
    print(i, end="  ")
else:
  for i in range(deagin, end - 1, -1):
    print(i, end="  ")