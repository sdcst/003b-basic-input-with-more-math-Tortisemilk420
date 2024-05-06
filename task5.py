#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

def calculate_future_population(current_population, growth_rate, days):
    
    r = growth_rate / 100.0
    
   
    time_in_years = days / 365.0
    
   
    future_population = current_population * (1 + r) ** time_in_years
    
    return int(round(future_population)) 

current_population = int(input("Enter the population: 25000000 "))
growth_rate = float(input("Enter the rate of growth in percent: 2.1 "))
days = int(input("Enter the number of days: 12 "))

future_population = calculate_future_population(current_population, growth_rate, days)

print(f"There will be {future_population} people after {days} days")

