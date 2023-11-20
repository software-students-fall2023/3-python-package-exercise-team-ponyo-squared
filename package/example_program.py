# Create an example program that uses all functions of your package and demonstrates its complete functionality.
from package_main.main import tracker,tracker_print,print_all_runtimes,save_to_file,entire_runtime

@tracker
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

@tracker_print
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

print("Factorial of 5:", calculate_factorial(5))
print("Fibonacci sequence up to 10:", fibonacci_sequence(10))

print_all_runtimes()

save_to_file("function_runtimes.txt")

entire_runtime()
