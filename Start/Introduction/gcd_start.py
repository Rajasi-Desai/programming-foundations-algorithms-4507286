# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    r = a%b
    while(r != 0):
        a = b
        b = r
        r = a%b
    return b


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
