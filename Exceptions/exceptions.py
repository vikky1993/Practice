# How to handle errors and exceptions in python

# try:
# 	f = open('testfile.txt')
# except Exception:
# 	print('Error!') # so this gives this error text msg as that file name does not exist


try:
	f = open('testfile.txt')
	# var = bad_var
except OSError as e:
	print(e)		# we have built in exceptions which can be used for particular exceptions
except Exception as e:
	print(e)
else:
	print(f.read()) # else clause runs only when we dont throw exceptions
	f.close()
finally:
	print("Executing Finally...")  # but finally clause runs whether we throwed exception or not

# We can use finally clause for an instance like closing the database even if we have caught exceptions



# We can raise our own exceptions too other than what system might find for us
try:
	f = open('corrupt_file.txt')
	if f.name == 'corrupt_file.txt':
		raise Exception
except OSError as e:
	print(e)		
except Exception as e:
	print('Error!')
else:
	print(f.read()) 
	f.close()	
finally:
	print("Executing Finally...")