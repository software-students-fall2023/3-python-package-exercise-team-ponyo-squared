import functools
import time
import colorama
from colorama import Fore

colorama.init()

def print_fancy_runtime(elapsed_time):
    print("\n")
    print(Fore.WHITE + "==========================================================" + Fore.RESET)
    print(Fore.WHITE + f"         Total runtime for the entire program            " + Fore.RESET)
    print(Fore.WHITE + f"         {elapsed_time * 1000:.4f} miliseconds           " + Fore.RESET)
    print(Fore.WHITE + "==========================================================" + Fore.RESET)
    print("\n")


# Dictionary to store function runtimes
function_runtimes = {}


start_time = time.time()

def tracker(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time() # recording the current time before executing the decorated function
        result = func(*args, **kwargs) # executing the decorated function
        end_time = time.time() # recording the current time after executing the decorated function
        elapsed_time = end_time - start_time # calculating the elapsed time
        function_name = func.__name__ # getting the name of the decorated function
        function_runtimes[function_name] = elapsed_time # storing the runtime in the dictionary
        return result # returning the result of the decorated function
    return wrapper # returning the wrapper function (the actual decorator)

def tracker_print(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time() # recording the current time before executing the decorated function
        result = func(*args, **kwargs) # executing the decorated function
        end_time = time.time() # recording the current time after executing the decorated function
        elapsed_time = end_time - start_time # calculating the elapsed time
        function_name = func.__name__ # getting the name of the decorated function
        function_runtimes[function_name] = elapsed_time # storing the runtime in the dictionary
        print(f"\n\nElapsed time of {function_name}: {elapsed_time * 1000:.4f} milliseconds") # returning the result of the decorated function
        return result # returning the result of the decorated function
    return wrapper # returning the wrapper function (the actual decorator)

def print_all_runtimes():
    print("\nAll tracked function runtimes:")
    total = 0
    for function_name, runtime in function_runtimes.items():
        total += runtime
        print(f"    Elapsed time of {function_name}: {runtime * 1000:.4f} milliseconds")
    print(f"The total runtime of tracked functions: {total * 1000:.4f} milliseconds")

def save_to_file(file_name):
    with open(file_name, 'w') as file:
        for function_name, runtime in function_runtimes.items():
            file.write(f"{function_name}: {runtime * 1000:.4f} milliseconds\n")
            #file.write(f"{function_name}: {runtime:.2f} seconds\n") # Write function names and runtimes to a file

# # decorator to print the runtime of all functions
# def AllRuntime(func):
#     @functools.wraps(func) # Use functools.wraps to preserve the original function's metadata
#     def wrapper(*args, **kwargs):
#         start_time = time.time() # Record the current time before executing the decorated function
#         result = func(*args, **kwargs) # Execute the decorated function
#         end_time = time.time() # Record the current time after executing the decorated function
#         elapsed_time = end_time - start_time # Calculate the elapsed time   

#         print("Function Runtimes:") # Print a header for the function runtimes
#         printAll() # Use the printAll() function to print the runtimes of all functions
#         print(f"Total Program Runtime: {elapsed_time * 1000:.2f} milliseconds") # Print the total program runtime
#         #print(f"Total Program Runtime: {elapsed_time:.2f} seconds") # Print the total program runtime
#         return result # Return the result of the decorated function
#     return wrapper # Return the wrapper function (the actual decorator)

def entire_runtime():
        end_time = time.time()
        elapsed_time = end_time - start_time
        cat = r'''
 /\_/\  
( o.o ) 
 > ^ < 
'''
        print(cat, end='') 

        print_fancy_runtime(elapsed_time)
        # print(f"Total runtime for the entire program: {elapsed_time * 1000:.4f} miliseconds meow!") 
