def adder(n: int):
  if n == 1:
    return n
  
  return n + adder(n - 1)


print(adder(int(input())))