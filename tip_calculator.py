try:	
	bill = float(input("What is the bill amount? "))
	if bill > 0:
		tip_percent = float(input("What is the tip percentage? ")) # this type is float because percent can be fractional
		if tip_percent >= 0:
			try:
				people = int(input("Between how many people will it be divided? "))
				if people > 0:
					tip_amount = bill / 100 * tip_percent
					tip_amount = round(tip_amount, 2)
					print("The tip is R$", tip_amount)
					total = bill + tip_amount
					total = round(total, 2)
					print("The total value is R$", total)
					per_person = total / people
					per_person = round(per_person, 2)
					print("Everyone will pay R$", per_person)
				else:
					print("Error: the number of people must be greater than zero")
			except ValueError:
				print("Error: the number of people must be a whole number.")
		else:
			print("Error: the tip percentage must be zero or greater.")
	else:
		print("Error: the bill must be greater than zero.")
except ValueError:
	print("Error: please type a valid number")
