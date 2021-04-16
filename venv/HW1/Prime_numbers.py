##Please write a program that print the first N prime numbers.
#N should be declared as a variable at the beginning of your code.

# this code does have a limit on the top range of primes. but I though it would be okay for this homework task
N=int(input("How many primes do you want? "))

def primes(N):
    # creating an empty list for the primes
	primes = []

	# loop from 2 to 15000 as 0 and 1 are niether a prime nor composite
	for i in range(2, 15000):

		# looping through the numbers i can be divided by
		for j in range(2, i):

			# To see if j divides evenly into i to see if its a prime or not
			if i % j == 0:
				break

		# if the loop exits without break then it should be a prime
		else:
			# so we can then append it to the list
			primes.append(i)

		# to stop adding more primes to the list we can add an if clause to match the number entered
		if len(primes) == N:
			return primes

print(primes(N))




