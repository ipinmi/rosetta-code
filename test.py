### 100 doors 

doors = [False] * 100

for i in range(100):
    # j moves in multiples of i + 1, starting from 0 to 100
    for j in range(i, 100, i+1):
        doors[j] = not doors[j]

        print("doors %d is" % (i+1), "opened" if doors[i] else "closed")


### 100 prisoners 
#best strategy is open the drawer with your number on it and follow it to the next drawer on the card 
# the maximum chain length needs to less than fifty boxes long.

from itertools import count
import random 

def play_at_random(n):
    #at first nobody is pardoned 
    pardoned = 0 
    # a sample of 100 numbers to select card numbers from 
    in_drawers = list(range(100))
    # for a randomized selection of numbers in the cycle 
    samplers = list(range(100))
    for _round in range(n):
        #shuffle the cards 
        random.shuffle(in_drawers)
        found = False
        for prisoner in range(100):
            found = False
            # selecting 50 random samplers since the max no of cycles is 50
            for card_reveal in random.sample(samplers, 50):
                card = in_drawers[card_reveal]
                #if you find your card, then you are set aside
                if card == prisoner:
                    found == True
                    break
            #when the 50th number is crossed, you are set aside too
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100

def play_optimal(n):
    pardoned = 0
    in_drawer = list(range(100))
    # for n number of prisoners
    for _round in range(n):
        random.shuffle(in_drawer)
        for prisoner in range(100):
            #go to your drawer number 
            reveal = prisoner 
            #asssuming nothing is found
            found = False
            for go in range(50):
                # go to the (prisoner number)th item in the in_drawer random list
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break 
                # the card in the drawer becomes the next drawer the prisoner goes to 
                reveal = card 
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100

if __name__ == '__main__':
    n = 100_000
    print(" Simulation count:", n)
    print(f" Random play wins: {play_at_random(n):4.1f}% of simulations")
    print(f"Optimal play wins: {play_optimal(n):4.1f}% of simulations") 

## The 10001th prime number
""" 
    A prime number is divisble by 1 and itself. Also greater than one. 
    Normal Logic: Divide by integer less than n, if there is no exact divisor then n is a prime number 
    Using Sieve of Eratosthenes: there is a list of integers from 2 to n. Cross the multiples of each prime number lesser than n one by one.
    Starting from 2,3,5,...
    Since there will be repetition in canceling the number, we optimize by checking for factors of that PN that are >= PN^2
    because factors < PN^2 will be striked out by smaller PNs
"""

def get_primes(s):
    """  
    Using Sieve of Eratosthenes to get a list of prime numbers less than s 

    Parameters
    ----------
    s : int
        number of prime numbers to return.

    Return
    ------
    primes: a byte-array of prime numbers.
         Each index corresponds to an integer in the list.
         A value of "1" at the index location indicates the integer is a prime.
    """
    #represents a list of integers from 1:s
    primes = bytearray([1] * s)
    # starting from 2 and ignoring 1 
    for i in range(2, s):
        # taking the ith number 
        if primes[i] == 1: 
            for j in range(i, s):
                # eg. if 2 * 2 is included in the range of s then the byte is replaced with 0
                # "cross out" factors by toggling elements from 1 to 0 at the corresponding index.
                if i*j < s:
                    primes[i*j] = 0 
                else: 
                    break
    return primes

def get_nth_prime(nth):
    """ 
    Parameters
    ----------
    s : int
        number of prime numbers to return.

    Return
    ------
    nth_prime: int
        the nth prime number 
    ------
    the integer list size has to be greater than "n" (the target prime number)
    we choose s = 2n initially, we generate all the primes < s using the sieve
    if the number of primes in the list is still less than n, then we increase the size of the list by n in the next iteration, until we find n 
    ** The Nth prime will be the number in the Nth position in the list after removing all the composites.
    
    """
    primes_count = 0 
    size_factor = 2 
    s = (nth * size_factor)
    while primes_count < nth:
        primes = get_primes(s)
        # excluding 0 and 1 
        primes_count = sum(primes[2:])

        size_factor += 1
        s = (nth * size_factor)

    nth_prime = count_primes(primes, nth)
    return nth_prime


def count_primes(primes, nth):
    """ 
    Returns the n-th prime represented by the index of the n-th "1" in the bytearray.
    """
    count = 0 
    for k in range(2, len(primes)):
        #since the values are "1"
        count += primes[k]
        if count == nth:
            return k 


def main():
    NTH_prime = 10001
    nth_prime = get_nth_prime(NTH_prime)
    print("The {}-th prime number is: {}".format(NTH_prime, nth_prime))

if __name__ == "__main__":
    main()