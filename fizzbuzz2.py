class FizzBuzz2:

        num1 = int(input("Please enter your fizz number: "))
        num2 = int(input("Please enter your buzz number: "))

        for i in range(1, 101):
            if (i % num1 == 0) and (i % num2 == 0):
                print("FizzBuzz")
            elif i % num1 == 0:
                print("Fizz")
            elif i % num2 == 0:
                print("Buzz")
            else:
                print(i)
            i += 1
