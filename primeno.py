from math import sqrt
from time import perf_counter,sleep  #pref_counter is used to calculate the time executed for the process
def primeno(): #convinent way of printing the prime number
    count1 = 0
    start_time = perf_counter()
    for c in range(2,100001):
        if c == 2:
            #print(c,end=',')
            flag=False
        if c > 2:
            flag=False
            for i in range(2, c//2+1):
                if (c % i ) == 0:
                    flag=True
                    break
            if flag!= True:
                count1=count1+1
                #print(count1)
    elapsed_time = perf_counter()- start_time
    print('\nprime no between 2 - 1001 :',count1+1)
    print('elapsed time in secs',elapsed_time)
#primeno()

def prime_eff():
    max_value = 1000
    count = 0
    value = 2  # Smallest prime number
    start = perf_counter()  # Start the stopwatch
    while value <= max_value:
            # See if value is prime
        is_prime = True  # Provisionally, value is prime
            # Try all possible factors from 2 to value - 1
        trial_factor = 2  ##3
        root = sqrt(value)
        while trial_factor <= root:
            if value % trial_factor == 0:
                is_prime = False  # Found a factor
                break  # No need to continue; it is NOT prime
            trial_factor += 1  # Try the next potential factor
        if is_prime:
            count += 1  # Count the prime number
        value += 1  # Try the next potential prime number

    sleep(5)
    elapsed = perf_counter() - start  # Stop the stopwatch
    print("Count:", count, " Elapsed time:", elapsed, "sec")
prime_eff()