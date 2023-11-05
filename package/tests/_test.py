from package_main.main import *

@tracker_print
def example_function():
    for i in range(1000):
        print("a")
@tracker_print
def example_function2():
    for i in range(2000):
        print("a")
@tracker_print
def example_function3():
    for i in range(3000):
        print("a")




@tracker
def test_example_function():
    result = example_function()
    result2 =example_function2()
    result3 = example_function3()

def test_printAll():
    print_all_runtimes()
    entire_runtime()

def test_printAll2(): 
    save_to_file("alex.txt")
    entire_runtime()

def test_printall3():
    print_all_runtimes()

def test_printall4():
    print_all_runtimes()
    entire_runtime()
    
