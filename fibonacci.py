k = int (input("Giveme a positive number: "))

def fibonacci (n):
    if n== 0 or n ==1:
        return n 
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    
for x in range (k):
    print(fibonacci(x))

plot(fibonacci(n))