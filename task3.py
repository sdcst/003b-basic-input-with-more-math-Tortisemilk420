#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

def calculate_total_price(items):
    subtotal = sum(items)
    tax_rate = 0.12  
    tax_amount = round(subtotal * tax_rate, 2)
    total_price = subtotal + tax_amount
    return subtotal, tax_amount, total_price

def main():
    print("Enter prices of 4 items:")

def new_func(calculate_total_price):
    
    new_func1(calculate_total_price)

def new_func1(calculate_total_price):
    new_func2(calculate_total_price)

def new_func2(calculate_total_price):

    
            item_prices = []
            for i in range(4):
                price = float(input(f"Enter price of item {i + 1}: $"))
                item_prices.append(price)

        
            subtotal, tax_amount, total_price = calculate_total_price(item_prices)

            print("\nSummary:")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Tax: ${tax_amount:.2f}")
            print(f"Total Price: ${total_price:.2f}")



   

