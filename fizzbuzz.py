class FizzBuzz:

    # for loop ranges over numbers from 1 to 100
    for i in range(1, 101):

        # if the number is a multiple of both 3 and 5, it prints out "FizzBuzz"
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")

        # if a multiple of 3 only, prints out Fizz
        elif i % 3 == 0:
            print("Fizz")

        # if a multiple of 5 only, prints out Buzz
        elif i % 5 == 0:
            print("Buzz")

        # if a multiple of neither, prints out the number
        else:
            print(i)

        # increments i by 1 in each loop until the end of the specified range
        i += 1
