def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	
	# Loop
	while amount_saved < down_payment:
	    amount_saved += amount_saved * (r / 12) + monthly_salary * portion_saved
	    months += 1
	    if months % 6 == 0:
	        yearly_salary *= (1 + semi_annual_raise)
	        monthly_salary = yearly_salary / 12
	
	# Output
	print("Number of months:", months)
	return months