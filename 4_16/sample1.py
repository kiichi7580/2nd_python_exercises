for i in range(100):
  if i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  else:
    print(i)

li = [1,1]
for i in range(100):
  a = li[i] + li[i + 1]
  li.append(a)

print(li)