st = 'python language is the best programming language'
for i in range(len(st)):
	end_val = '-'
	if st[i] == ' ':
		end_val = ''
	if i == len(st)-1:
		end_val = ''
	elif st[i+1] == ' ':
		end_val = ''

	# print(st[i].upper(), end=end_val)
	if i%2 == 0:
		print(st[i].upper(), end=end_val)
	else:
		print(st[i].lower(), end=end_val)
