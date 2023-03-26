q = int(input())
w = int(input())
if q > w:
  q, w = w, q
print("------")
for i in range(q, w + 1):
  if i % 5 == 0 and i % 3 == 0:
    print("Fizz Buzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  else:
    print(i)
