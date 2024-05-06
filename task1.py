#!python3
 
"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.2 interest. 
(2 points) 
"""
def calculate_interest(principal, rate, days_in_month):

    rate_decimal = rate / 100
    
    interest = principal * rate_decimal * (days_in_month / 365)
    
    return interest


principal = float(input("Enter your amount: "))
rate = float(input("Enter the rate (as a percentage): "))
days_in_month = int(input("Enter the number of days in the month: "))


interest_earned = calculate_interest(principal, rate, days_in_month)


print(f"You earned ${interest_earned:.2f} interest.")
