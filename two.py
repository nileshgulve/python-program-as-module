#!/usr/bin/python3
import one
def main():
	one.main()
	print('=' * 50)
	print("The value __name__ is:",__name__)
if __name__ == '__main__':
	main()

# Output:
# ./two.py 
# The value __name__ is: one
# ==================================================
# The value __name__ is: __main__
