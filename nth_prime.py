def nth_prime(n: int):
    """
    n: int
    This program returns the nth prime number that a user gives 
    If user input is invalid, program returns -1. 
    >>> nth_prime(1):
    2
    >>> nth_prime(2):
    3
    >>> nth_prime(4):
    7
    """

    dict_of_primes = {'1': 2} #This is the initial start for the dictionary, and it is the first prime number
    num_to_check = 3
    counter = 1

    while len(dict_of_primes) != n:

        for key_prime in dict_of_primes:
            if (num_to_check % dict_of_primes[key_prime]) == 0:
                break #We stop once a number is divisible by a prime,
                      #as that means that it is not prime 
    
        else:
            counter += 1 #This serves in being the dictionary's key
            dict_of_primes.update({str(counter): num_to_check})
        num_to_check += 1 #This is to check the next number
    
    print(dict_of_primes)
    return dict_of_primes[str(n)]  #This will convert the n to a string to get it from the dictionary, then return it

