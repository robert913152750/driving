country = input('你是哪國人?')
age = input('請問你今年幾歲?')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')
		

