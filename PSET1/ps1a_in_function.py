def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	
	# Constants
	portion_down_payment = 0.25
	r = 0.05  # annual return
	
	# Variables
	monthly_salary = yearly_salary / 12
	amount_saved = 0.0
	months = 0
	down_payment = cost_of_dream_home * portion_down_payment
	
	###############################################################################################
	## Determine how long it takes to save for a down payment ##
	###############################################################################################
	
	# Loop until enough savings
	while amount_saved < down_payment:
	    amount_saved += amount_saved * (r / 12) + monthly_salary * portion_saved
	    months += 1
	
	# Output
	print("Number of months:", months)
	return months