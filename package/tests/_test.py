from package_main.main import tracker, tracker_print, printAll, entire_Runtime

@tracker
def example_function():
    for i in range(1000):
        i = i * 2
    return("Test function executed")

@tracker_print
def example_function2():
    for i in range(10000):
        i = i * 2
    return("Test function executed")

@entire_Runtime
def test_example_function():
    result = example_function()
    result2 = example_function2()
    assert result == "Test function executed"
    assert result2 == "Test function executed"
    print("example_function executed successfully")

# def test_printAll():
#     printAll()
