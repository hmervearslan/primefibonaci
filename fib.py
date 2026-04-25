def fibonacci(m):
    a, b = 0, 1
    result = []
    while b < m:
        result.append(b)
        a, b = b, a + b
    return result

def prime(n): 
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
 
 
def list_prime(list): 
	prime_list =[ ] 
	for i in list: 
		x = prime(i) 
		if x == True: 
			prime_list.append(i) 
	return prime_list 

# command that find prime numbers is Fibonacci sequence from 0 to m	 
m =int(input("find prime numbers is Fibonacci sequence from 0 to m. What is the m you want?: "))
print(list_prime(fibonacci(m))) 
