# Use else to execute code after a for loop concludes
# python's for loop can include an else clause
# It is executed after the iterator is exhausted, unless the loop was ended prematurely due to a break statement

## Harmful

for user in get_all_users():
	has_malformed_email_address = False
	print('Checking {}'.format(user))
	for email_address in user.get_all_email_addresses():
		if email_is_malformed(email_address):
			has_malformed_email_address = True
			print('Has a malformed email address!')
			break
	if not has_malformed_email_address:
		print('All email addresses are valid!')


## Idiomatic

for user in get_all_users():
	print('Checking {}'.format(user))
	for email_address in user.get_all_email_addresses():
		if email_is_malformed(email_address):
			print('Has a malformed email address!')
			break
	else:
		print('All email addresses are valid!')