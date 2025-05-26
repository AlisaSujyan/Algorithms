def factorial(n, memory={}):
  if n == 0 or n == 1:
    return 1
  if n in memory:
    return memory[n]
  memory[n] = n * factorial(n - 1, memory)
  print(memory)
  return memory[n]

print(factorial(7))

print(factorial(5))

print(factorial(10))