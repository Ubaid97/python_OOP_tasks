class FizzBuzz2:

        # users are asked to input the two numbers for which they'd like fizz and buzz substituted
        num1 = int(input("Please enter your fizz number: "))
        num2 = int(input("Please enter your buzz number: "))

    # for loop ranges over numbers from 1 to 100
        for i in range(1, 101):

            # if the number is a multiple of both numbers passed by the user, it prints out "FizzBuzz"
            if (i % num1 == 0) and (i % num2 == 0):
                print("FizzBuzz")

            # if a multiple of the first number only, prints out Fizz
            elif i % num1 == 0:
                print("Fizz")

            # if a multiple of the second number only, prints out Buzz
            elif i % num2 == 0:
                print("Buzz")

            # if a multiple of neither, prints out the number
            else:
                print(i)

            # increments i by 1 in each loop until the end of the specified range
            i += 1
