arr = ['aaa', 'bbb','ccc', 'aaaa', 'bbbb', 'cccc', 'gddgj', 'gsgrh','jdxsg', 'hkbdrs','bxssef','1dwthi','jbsrhxs','zctshnk','vshxseg','axgkncdh','&bsrkcdj','gjxaftxj','vxsgvkxae','vjzahvkst','awdjlczar','agvkdatvks','@&gzhaj876','adkyxjstjf','ozwi8cwu5v']
def welcome():
	print('Welcome to password generator')
def function1():
	num = int(input('Enter a length between 3 and 10 :'))
	while num < 3:
		num = int(input('Length cannot be less than 3! Enter length again :'))
	while num > 10:
		num = int(input('Length cannot be greater than 10 please! enter length again   :'))
	return num
def function2():
	count = 0
	while count < 3:
		given = []
		for i in arr:
			if len(i) == num1:
				given.append(i)
				count = count + 1
				if count ==3:
					return given
def generator():
	count = 0
	while count < 3:
		print('Password is ' +first[count])
		x = input('Satisfied? ')
		if x == 'yes':
			print('Password is '+str(first[count]))
			break
		if x == 'no':
			count = count + 1
			if count == 3:
				print('Out of possible passwords for the length '+str(num1))
		

welcome()
num1 = function1()
first = function2()
generator()



