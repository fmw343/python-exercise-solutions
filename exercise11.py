def get_integer():
    return int(input("Give me a number: "))

def check_prime(number):
    divisors = []
    for x in range(2, number - 1):
        if number % x == 0:
            divisors.append(x)
    
    if len(divisors) > 0:
        print(f"{number} is not a prime.")
    else:
        print(f"{number} is a prime.")
        
num = get_integer()
check_prime(num)
