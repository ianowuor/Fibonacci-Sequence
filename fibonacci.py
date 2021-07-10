# A function to generate Fibonacci numbers
def generate_fibonacci_numbers():
    fnumbers = [0, 1]  # A variable containing the first two Fibonacci numbers
    for numbers in range(1, 100):  # Add the range that you want to generate the Fibonacci numbers through
        new_number = fnumbers[len(fnumbers) - 1] + fnumbers[len(fnumbers) - 2]
        fnumbers.append(new_number)

    for number in fnumbers:  # Prints all the numbers in the fnumbers list
        print(number)

generate_fibonacci_numbers()  # Calling the generate Fibonacci numbers function



