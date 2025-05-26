def Fibonacci(n, memory={}):
  if n == 0:
    memory[0] = 0
    return 0
  if n == 1 or n == 2:
    memory[1] = 1
    memory[2] = 1
    return 1
  if n in memory:
    return memory[n]
  memory[n] = Fibonacci(n - 1, memory) + Fibonacci(n - 2, memory)
  print(memory)
  return memory[n]


print(Fibonacci(7))
print(Fibonacci(5))
print(Fibonacci(10))