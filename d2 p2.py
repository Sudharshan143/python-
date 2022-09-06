def check(S , T):
	if(sorted(S)== sorted(T)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		
		

S = str('sudharshan: ')
T = str('sudharshan: ')
check(S , T)
