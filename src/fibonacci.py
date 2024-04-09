
def fibonacci (n):
    if n== 0 or n ==1:
        return n 
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    
if __name__ == "__main__":
    k = int(input("Give me a positive number: "))
    h = k - 1
    print(fibonacci(h))

