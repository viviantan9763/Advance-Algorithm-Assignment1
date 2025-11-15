
# Question 3: Concurrent Factorial Calculation
# Using Multithreading vs Single Thread

import threading   # Python module to create threads
import time        # Python module to measure time

# 1. Factorial Function
def factorial(n):
    #Calculates factorial of n iteratively.
    #Big-O: O(n), since it multiplies n numbers.
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 2. Factorial with Thread
def factorial_thread(n, results, index):
    #Thread target function: calculates factorial(n)
    results[index] = factorial(n)


# 3. Multithreading Execution
def run_multithreading(numbers):
    #Runs factorial calculations in parallel using separate threads.
    threads = []
    results = [None] * len(numbers)  # Shared list to store results

    start_time = time.perf_counter_ns()  # Start time in nanoseconds

    # Create and start a thread for each number
    for i, num in enumerate(numbers):
        t = threading.Thread(target=factorial_thread, args=(num, results, i))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    end_time = time.perf_counter_ns()  # End time in nanoseconds
    total_time = end_time - start_time
    return results, total_time

# 4. Single Thread Execution
def run_singlethread(numbers):

    #Runs factorial calculations sequentially (no threads).

    results = []
    start_time = time.perf_counter_ns()

    for num in numbers:
        results.append(factorial(num))

    end_time = time.perf_counter_ns()
    total_time = end_time - start_time
    return results, total_time

# 5. Menu-Driven Program
choice = 0
numbers_to_compute = [50, 100, 200]  # Factorials to calculate

while choice != 5:
    print("\n--- Concurrent Factorial Menu ---")
    print("1. Calculate factorials with multithreading")
    print("2. Calculate factorials with single thread")
    print("3. Run 10 rounds of multithreading test")
    print("4. Run 10 rounds of single thread test")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number.")
        continue

    # 1. Single multithreading run
    if choice == 1:
        results, total_time = run_multithreading(numbers_to_compute)
        print("Results:", results)
        print(f"Total time (ns): {total_time}")

    # 2. Single sequential run
    elif choice == 2:
        results, total_time = run_singlethread(numbers_to_compute)
        print("Results:", results)
        print(f"Total time (ns): {total_time}")

    # 3. 10 rounds multithreading test
    elif choice == 3:
        print("Running 10 rounds of multithreading test...")
        total_times = [] #Create an empty list to store time taken
        for i in range(10):
            results, t = run_multithreading(numbers_to_compute)
            total_times.append(t)#Save the time to total_time list
            print(f"Round {i+1}: {t} ns")
        avg_time = sum(total_times) // len(total_times)
        print("Average time (ns):", avg_time)

    # 4. 10 rounds single-thread test
    elif choice == 4:
        print("Running 10 rounds of single-thread test...")
        total_times = []
        for i in range(10):
            results, t = run_singlethread(numbers_to_compute)
            total_times.append(t)
            print(f"Round {i+1}: {t} ns")
        avg_time = sum(total_times) // len(total_times)
        print("Average time (ns):", avg_time)

    # 5. Exit
    elif choice == 5:
        print("Exiting program. Goodbye!")

    else:
        print("Invalid choice. Try again.")

