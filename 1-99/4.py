# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

def is_palindrom(digit):
	asString = str(digit)

	for i in xrange(0, len(asString)/2):
		if asString[i] != asString[-i-1]:
			return False

	return True

def findMax(red):
	maxLimit = pow(10, red) - 1
	minLimit = pow(10, red-1) -1

	answer = 0
	for i in xrange(maxLimit, minLimit, -1):
		for j in xrange(maxLimit, minLimit, -1):
			mult = i*j
			if is_palindrom(mult):
				if answer < mult:
					answer = mult

	return answer

def main():
	print findMax(3)


main()