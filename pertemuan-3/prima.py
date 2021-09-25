def isPrime(number):
    if number > 1:
        for x in range(2,number):

            print(number, '%', x, '=', number % x)
            if(number % x == 0):
                return False
        return True
        

def primeList(list):

    prime_list = []
    not_prime = []

    for number in list:
        if number > 1:
            if(isPrime(number)):
                prime_list.append(number)
            else:
                not_prime.append(number)

            
    return {
        'prime_list' : prime_list,
        'not_prime' : not_prime
    }

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(primeList(list))