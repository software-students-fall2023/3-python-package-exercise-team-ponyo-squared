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