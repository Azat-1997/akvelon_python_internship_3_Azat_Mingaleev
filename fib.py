def fib(n:int) -> int:
    if n < 0:
       raise ValueError("number should be natural")

    else:
       x = 0
       y = 1
       for i in range(n):
           x, y = y, x + y

       return x

if __name__ == "__main__":
   print(fib(0))
   print(fib(7))
   print(fib(-1))
