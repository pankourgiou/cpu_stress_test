import time
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Function to perform CPU stress test
def cpu_stress_test(limit):
    print(f"Starting CPU stress test with limit {limit}...")
    
    start_time = time.time()
    prime_count = 0
    for num in range(2, limit):
        if is_prime(num):
            prime_count += 1
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Found {prime_count} primes in the range 2 to {limit}.")
    print(f"Time taken: {elapsed_time:.2f} seconds")

# Running the CPU test with a configurable limit
if __name__ == "__main__":
    limit = int(input("Enter the upper limit for prime number calculation: "))
    cpu_stress_test(limit)
