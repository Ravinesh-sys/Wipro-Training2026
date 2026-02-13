import math
import time
import multiprocessing

numbers = [50000, 60000, 55000, 45000, 70000]

# Function to calculate factorial
def calculate_factorial(n):
    return math.factorial(n)

# VERY IMPORTANT FOR WINDOWS
if __name__ == "__main__":

    # Sequential
    start_seq = time.time()

    seq_results = []
    for num in numbers:
        result = calculate_factorial(num)
        seq_results.append(result)
        print(f"Factorial of {num} calculated")

    end_seq = time.time()
    print("Sequential Time:", end_seq - start_seq, "seconds")

    # Multiprocessing
    start_mp = time.time()

    with multiprocessing.Pool() as pool:
        mp_results = pool.map(calculate_factorial, numbers)

    for num in numbers:
        print(f"Factorial of {num} calculated")

    end_mp = time.time()
    print("Multiprocessing Time:", end_mp - start_mp, "seconds")
