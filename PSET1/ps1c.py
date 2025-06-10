## 6.100A PSet 1: Part C
## Name: Matias Ezequiel Petenatti
## Time Spent: 0:30
## Collaborators:

##############################################
## Get user input for the three variables below ##
##############################################

initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

# Constants
cost = 800000
down_payment = 0.25 * cost  # $200,000
months = 36
epsilon = 100

# Variables for bisection search
low = 0.0
high = 1.0  # 100% annual rate
steps = 0
r = None

##################################################################################################
## Determine how long it takes to save for a down payment ##
##################################################################################################

# Check if initial deposit is already sufficient (within $100 of target)
if initial_deposit >= down_payment - epsilon:
    r = 0.0
else:
    # Check if it's impossible even with 100% return rate
    max_amount = initial_deposit * ((1 + high / 12) ** months)
    if max_amount < down_payment - epsilon:
        r = None
    else:
        # Bisection search
        while low <= high:
            guess = (low + high) / 2.0
            amount_saved = initial_deposit * ((1 + guess / 12) ** months)
            steps += 1
            
            # Check if we're within the acceptable range
            if abs(amount_saved - down_payment) <= epsilon:
                r = guess
                break
            elif amount_saved < down_payment:
                low = guess
            else:
                high = guess
            
            # Stop if the range is small enough
            if high - low < 1e-10:
                break

# Output
if r is None:
    print("Best savings rate: None")
else:
    print("Best savings rate:", r)
print("Steps in bisection search:", steps)