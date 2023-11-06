from package_main.main import *

@tracker_print
def example_function():
    for i in range(1000):
        i += 1
        i -=1
@tracker_print
def example_function2():
    for i in range(2000):
        i += 1
        i -=1
@tracker_print
def example_function3():
    for i in range(3000):
        i += 1
        i -=1




@tracker
def test_example_function():
    result = example_function()
    result2 = example_function2()
    result3 = example_function3()

def test_printAll():
    print_all_runtimes()
    print("\n-------------------------------------------------------------------------------------------------\n")

def test_printAll2(): 
    save_to_file("alex1.txt")
    print_all_runtimes() 
    print("\n-------------------------------------------------------------------------------------------------\n")
    
def test_printall3():
    tracker_print(example_function2())
    print_all_runtimes()
    print("\n-------------------------------------------------------------------------------------------------\n")

def test_printall4():
    print_all_runtimes()
    entire_runtime()
    print("\n-------------------------------------------------------------------------------------------------\n")
    
def test_saveTo1():
    #testing saving to a file that doesn't exist
    save_to_file("alex.txt")
    #giving the file some example info to put in
    entire_runtime()
    print("\n-------------------------------------------------------------------------------------------------\n")
def test_saveTo2():
    #testing saving to a file that already exists
    save_to_file("alex.txt")
    #saving nothing
    print("\n-------------------------------------------------------------------------------------------------\n")
def test_saveTo3():
    #testing saving to a file that already exists
    save_to_file("alex.txt")
    #saving some info
    entire_runtime()
    print("\n-------------------------------------------------------------------------------------------------\n")
def test_saveTo4():
    print_fancy_runtime(5)#random number
    save_to_file("alex2.txt")
    print_fancy_runtime(2)#random number
    #I.E. save_to_file is unaffected by other prints before or after its run
    print("\n-------------------------------------------------------------------------------------------------\n")

