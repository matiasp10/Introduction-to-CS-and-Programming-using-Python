## 6.100A PSet 1: Part C
## Name: Matias Ezequiel Petenatti
## Time Spent: 0:30
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

house_cost = 800000
down_payment = house_cost * 0.25
months = 36
l = 0
u = 1
r = (l + u) / 2 
epsilon = 100 
steps = 0
cint = lambda money,r,months: money*( (1 + r / 12) ** months )

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

if initial_deposit > down_payment:
    r = 0
elif cint(initial_deposit, u, months) >= down_payment:
    steps += 1
    while abs(cint(initial_deposit, r, months) - down_payment) >= epsilon:
        if cint(initial_deposit, r, months) < down_payment:
            l = r
        else:
            u = r
        steps += 1
        r = (l + u) / 2 
else:
    r = None
print(f'Best savings rate: {r}')
print(f'Steps in bisection search: {steps}')