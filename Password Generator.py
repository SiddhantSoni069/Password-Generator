#  Password Generator
import random

print(':===== Password Generator =====:')

upper_char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeric_char = [1,2,3,4,5,6,7,8,9,0]
special_char = "!@#$%^&*()_-+=:;{[]}<,>.?/"


def randomizer():

	#  taking input from the user for length of password

	password_len = input("Select password length (0-8->a / 8-16->b / 16-20->c): ")
	
	if (password_len == 'a'):
		for i in range(0,2): #This loop runs twie
			upper_char_random = random.randint(0,len(upper_char)-1)
			print(upper_char[upper_char_random],end = '')

			lower_char_random = random.randint(0,len(lower_char)-1)
			print(lower_char[lower_char_random],end = '')

			numeric_char_random = random.randint(0,len(numeric_char)-1)
			print(numeric_char[numeric_char_random],end = '')

			special_char_random = random.randint(0,len(special_char)-1)
			print(special_char[special_char_random],end = '')

	elif (password_len == 'b'):
		for i in range(0,3):
			upper_char_random = random.randint(0,len(upper_char)-1)
			print(upper_char[upper_char_random],end = '')

			lower_char_random = random.randint(0,len(lower_char)-1)
			print(lower_char[lower_char_random],end = '')

			numeric_char_random = random.randint(0,len(numeric_char)-1)
			print(numeric_char[numeric_char_random],end = '')

			special_char_random = random.randint(0,len(special_char)-1)
			print(special_char[special_char_random],end = '')
	else:
		for i in range(0,4):
			upper_char_random = random.randint(0,len(upper_char)-1)
			print(upper_char[upper_char_random],end = '')

			lower_char_random = random.randint(0,len(lower_char)-1)
			print(lower_char[lower_char_random],end = '')

			numeric_char_random = random.randint(0,len(numeric_char)-1)
			print(numeric_char[numeric_char_random],end = '')

			special_char_random = random.randint(0,len(special_char)-1)
			print(special_char[special_char_random],end = '')
		
def quitter(): #  Function that terminates the program when any key from the keyboard is pressed
	a=input("\n\nPress any key to exit")
	quit()

randomizer()
quitter()