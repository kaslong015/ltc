bank_name = "GtBank"
attempt = 3
password = 1234
balance = float(round(5000,2))

menu = {1:"balnace",2:"withdrawal",3:"exit"}

while attempt > 0:
	user_pin = int(input('enter pin\n'))

	if(user_pin == password):
		for key,value in menu.items():
			print("enter {} for {}".format(key,value))
		option = int(input("enter option value\n"))

		if option == 1:
			print("your balance is : ",balance)
		elif option == 2:
			withdrawal_amount = int(input("enter amonut\n"))

			if(withdrawal_amount > balance):
				print("insufficient Fund")
				break
			elif (balance - withdrawal_amount) <= 500:
				print("insufficient Fund ")
				print("do you want to carry out another transaction Y or N")
				res = input("enter Y or N \n")
				if(res == "N"):
					break
			else:
				balance -= withdrawal_amount
				print("take your cash your balance is " ,balance)
				print("do you want to carry out another transaction Y or N")
				res = input("enter Y or N \n")
				if(res == "N"):
					break
		elif option == 3:
			break
	else:
		print("wrong pin")
		attempt -= 1
print("thanks for using GtBank ","\U0001f600 "*5)
	