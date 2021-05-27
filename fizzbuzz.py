def fizz_buzz(num):
    result = ""
    # I have no idea how to return a string, so Ima just make the if statements edit an empty one
    if(num % 3 == 0 and num % 5 == 0):
        result = result + "FizzBuzz"
        return result
    # apparently the FizzBuzz statement has to go first, otherwise the 3 or 5 will always be calculated to be true first, and run first
    if(num % 3 != 0 and num % 5 != 0):
        result = result + str(num)
        return result
    # I returned the num by itself if it doesn't meet the fizz_buzz condition. Also I made it go before the single conditions just to be safe
    if(num % 3 == 0):
        result = result + "Fizz"
        return result
    if(num % 5 == 0):
        result = result + "Buzz"
        return result