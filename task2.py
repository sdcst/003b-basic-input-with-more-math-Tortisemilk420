#!python3
"""
Assignment: Exchange rate
The current exchange rate is 1.25 CAD per 1 USD
Create a program that asks the user for the number of Canadian Dollars they have
and then have the program display how many USD that is equivalent to:
You may need to use rounding or decimal formatting


example
How many Canadian Dollars do you have? 10
That is worth $8.00 USD

How many Canadian Dollars do you have? 1.25
That is worth $1.00 USD
"""

exchange_rate = 1.25  

def get_canadian_dollars():
    while True:
        try:
            canadian_dollars = float(input("How many Canadian Dollars do you have? "))
            return canadian_dollars
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    canadian_dollars = get_canadian_dollars()
    usd_amount = canadian_dollars / exchange_rate
    formatted_usd_amount = f"${usd_amount:.2f}"  
    print(f"That is worth {formatted_usd_amount} USD")


