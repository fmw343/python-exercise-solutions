def get_integer():
    return int(input("Give me a number: "))

def check_prime(number):
    is_prime = True
    
    if number < 2:
        print(f"{number} is not a prime.")
        return
    
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
            print(f"{number} is not a prime.")
            break
        
    if is_prime == True:
        print(f"{number} is a prime.")
 
num = get_integer()
check_prime(num)
