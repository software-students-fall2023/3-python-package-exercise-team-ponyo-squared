import time # Import the time module for timing functions
import functools # Import the functools module for working with decorators


# Dictionary to store function runtimes
function_runtimes = {}


def tracker(func):
    @functools.wraps(func) # using functools.wraps to preserve the original function's metadata
    def wrapper(*args, **kwargs):
        start_time = time.time() # recording the current time before executing the decorated function
        result = func(*args, **kwargs) # executing the decorated function
        end_time = time.time() # recording the current time after executing the decorated function
        elapsed_time = end_time - start_time # calculating the elapsed time
        function_name = func.__name__ # getting the name of the decorated function
        function_runtimes[function_name] = elapsed_time # storing the runtime in the dictionary
        return result # returning the result of the decorated function
    return wrapper # returning the wrapper function (the actual decorator)


def printAll():
    for function_name, runtime in function_runtimes.items():
        print(f"{function_name}: {runtime * 1000:.2f} milliseconds")
        #print(f"{function_name}: {runtime:.2f} seconds") # Print the name and runtime of each function


def saveToFile(file_name):
    with open(file_name, 'w') as file:
        for function_name, runtime in function_runtimes.items():
            file.write(f"{function_name}: {runtime * 1000:.2f} milliseconds\n")
            #file.write(f"{function_name}: {runtime:.2f} seconds\n") # Write function names and runtimes to a file


# Decorator to print the runtime of all functions
def AllRuntime(func):
    @functools.wraps(func) # Use functools.wraps to preserve the original function's metadata
    def wrapper(*args, **kwargs):
        start_time = time.time() # Record the current time before executing the decorated function
        result = func(*args, **kwargs) # Execute the decorated function
        end_time = time.time() # Record the current time after executing the decorated function
        elapsed_time = end_time - start_time # Calculate the elapsed time   

        print("Function Runtimes:") # Print a header for the function runtimes
        printAll() # Use the printAll() function to print the runtimes of all functions
        print(f"Total Program Runtime: {elapsed_time * 1000:.2f} milliseconds") # Print the total program runtime
        #print(f"Total Program Runtime: {elapsed_time:.2f} seconds") # Print the total program runtime
        return result # Return the result of the decorated function
    return wrapper # Return the wrapper function (the actual decorator)