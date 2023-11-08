# Runtime Ponyo
Times the execution of functions while providing users to save and display recorded runtimes

## Installation 

Import the provided functions from `main.py` into your Python script.
`from  package_main.main  import  *`

##  Functionalities

`@tracker`
When this decorator is applied to a function, Runtime Ponyo begins to time that functions execution.

`@tracker_print`
When this decorator is applied to a function, Runtime Ponyo begins to time that functions execution *and* displays the runtime upon completion.   

`'print_all_runtimes()'`
All runtimes recorded are displayed.

> This only print the runtimes of functions that have been completed and tracked **prior** to the call of this  function.

`save_to_file(file.txt)`
This function saves the recorded runtimes to a specified file. If the file doesn't exist, it will be created with the given name, and the runtime data will be written to it.

`'entire_runtime()'`
Calculates and prints the total runtime of the entire program.

## Usage

To use `@tracker_print`, apply the decorator to a  function

```
@tracker
def  example_function():
	for  i  in  range(1000):
		i  +=  1
```
##
To use `@tracker_print`, apply the decorator to a  function
```
@tracker_print
def  example_function():
	for  i  in  range(1000):
		i  +=  1
```
##
Insert the `print_all_runtimes()` function at the desired location in your program to use it

```
analyzed_data  = complex_data_analysis(pd.concat(processed_chunks))

print_all_runtimes() # Track and print function runtimes

log_operations(datetime.now())
print(f"Analyzed Data: \n{analyzed_data}")
```
##
Insert the `save_to_file()` function at the desired location in your program to use it
```
with ThreadPoolExecutor(max_workers=4) as  executor:
	future_to_chunk  = {executor.submit(advanced_data_transformation, chunk): chunk  for  chunk  in  chunks}


save_to_file(my_runtimes.txt) # Save recorded runtimes to a specified file

processed_data  = [future.result() for  future  in  future_to_chunk]
```
##
Insert the `'entire_runtime()'` function at the desired location in your program to use it
```
data  = np.random.exponential(scale=1.0, size=(1000, 2))
df  = pd.DataFrame(data, columns=['id', 'values'])

chunks  = np.array_split(df, 4)

entire_runtime() # Print the total runtime of the program
```
##




A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.
