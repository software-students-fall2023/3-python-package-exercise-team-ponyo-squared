from package_main.main import *

@tracker_print
def example_function():
    for i in range(1000):
        print("a")

@tracker
def test_example_function():
    result = example_function()

def test_printAll():
    print_all_runtimes()
    entire_runtime()

def test_printAll2():
    save_to_file("alex.txt")
    entire_runtime()
