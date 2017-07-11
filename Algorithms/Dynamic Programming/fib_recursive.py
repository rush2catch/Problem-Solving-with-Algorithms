
class Solution(object):

	def fib_recursive(self, n):
		if n < 0:
			return -1
		if n == 1 or n == 0:
			return 1
		return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

	def fib_linear(self, n):
		if n < 0:
			return -1
		if 0 <= n <= 1:
			return 1
		answer = 1
		last = 1
		nextToLast = 1
		for i in range(2, n+1):
			answer = last + nextToLast
			nextToLast = last
			last = answer
		return answer

	def print_fib(self, n):
		for i in range(n):
			# print("fib({}) = {}".format(i, self.fib(i)), end = ' ')
			print(self.fib_recursive(i), end=' ')
		print()
		for i in range(n):
			print(self.fib_linear(i), end=' ')

obj = Solution()
obj.print_fib(20)