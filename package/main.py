from package_main import tracker, printAll, saveToFile, AllRuntime
@tracker
def example_function():
    x = 10
    for i in range(10000):
        x += i

@AllRuntime
def main():
    example_function()
    #other

if __name__ == "__main__":
    main()
