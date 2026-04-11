numbers = [1, 2, 3, 4, 5]
numbers_cubic = map(lambda number: number ** 3, numbers)
print(list(numbers_cubic))

emails = ['marcioalexis@gmail.com', 'marcioalexis@outlook.com', 'marcioalexis@yahoo.com']
providers = list(map(lambda email: email.split(sep="@")[-1], emails))

print(providers)

#Function map with a defined function
years = [10,15,20,25,30]
tax = [0.1, 0.15, 0.2, 0.25, 0.3, 0.05]
initial_values = [1000, 2000, 3000, 4000, 5000]

def calculate_final_insvestment(initial_value, tax, years):
    final_value = initial_value
    for year in range(years):
        final_value += final_value * tax
    return round(final_value, 2)

scenarios = list(map(calculate_final_insvestment, initial_values, tax, years))
print(scenarios)
