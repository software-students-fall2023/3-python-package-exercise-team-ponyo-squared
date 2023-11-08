
### Runtime Ponyo
Times the execution of functions while providing users to save and display recorded runtimes

### Installation 

Import the provided functions from `main.py` into your Python script.
`from  package_main.main  import  *`

###  Functionalities and Usage

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
