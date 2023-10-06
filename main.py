# This script will play FizzBuzz
# https://en.wikipedia.org/wiki/Fizz_buzz
# from 1 to GAME_LENGTH (inclusive).

GAME_LENGTH = 100

for num in range(1, GAME_LENGTH+1):
    if num % 3 == 0:
        print("Fizz")
    else:
        print(num)
    if num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Expected output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# (and so on...)
