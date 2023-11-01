from package_main import tracker, printAll, saveToFile, AllRuntime


@tracker
def example_function():
# TBW


@AllRuntime
def main():
example_function()
# can also put the functions to be tested here


if __name__ == "__main__":
main()

