"""
Project Euler, Problems 1-2

Problem 1:
Find the sum of all multiples of 3 or 5 under 1000.

Problem 2:
Find the sum of all even Fibonacci numbers under 4000.

Author:  Alicia Bargar/boomdigs
"""

import time

#Problem 1

start = time.time()

id1Sum = 0

for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        id1Sum += i
print "Problem 1 sum: {0}".format(id1Sum)

end = time.time()
print "Time taken: {0}".format(round(end - start,3))

#Alternative/faster solution for 1
start = time.time()
print "Problem 1 sum: {0}".format(sum([i for i in range(0,1000) if i%3 == 0 or i%5 == 0]))
end = time.time()
print "Time taken: {0}".format(round(end - start,3))


#Problem 2
start = time.time()

fib1 = 1
fib2 = 2
evenFibSum = 0

while fib2 <= 4000000:
    if fib2 % 2 == 0:
        evenFibSum += fib2
    fib2 = fib1 + fib2
    fib1 = fib2 - fib1
print "Problem 2 solution: {0}".format(evenFibSum)
end = time.time()
print "Time taken: {0}".format(round(end - start,3))
