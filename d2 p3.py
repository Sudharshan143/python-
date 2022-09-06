

import math
number = int(input("enter the number"))

root = math.sqrt(number)
if int(root + 0.5) ** 2 ==number:
    print(number,"is a perfect square")

else:
        print(number, "is not a perfect square")



# Python3 program to check if a number is
# perfect square without finding square root

# from math import sqrt function


def isPerfectSquare(n) :

	i = 1
	while(i * i<= n):
		
		# If (i * i = n)
		if ((n % i == 0) and (n / i == i)):
			return True
			
		i = i + 1
	return False

# Driver code
if __name__ == "__main__" :

	number = int(input("enter the number"))
	if (isPerfectSquare(n)):
		print("true, it is a perfect square.")
	elif n == 0:
		print("true, it is a perfect square.")
	else :
		print("false, it is not a perfect square.")

	# This code is contributed by Ryuga



