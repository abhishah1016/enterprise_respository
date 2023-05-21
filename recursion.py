def fact(no):
	if(no == 1):
		return no;
	else:
		return no * fact(no-1);


print("Enter any number to get factorial:");
no = int(input());

ans = fact(no);
print("factorial of number:",ans);

