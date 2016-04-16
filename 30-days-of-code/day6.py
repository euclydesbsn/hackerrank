for _ in range(int(raw_input())):
	s = raw_input()
	s_array = [abs(ord(s[i+1])-ord(s[i])) for i in range(0,len(s)-1)]
	if s_array == s_array[::-1]:
		print "Funny"
	else:
		print "Not Funny"