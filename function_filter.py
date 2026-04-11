numbers = []
for i in range(1,61):
    numbers.append(i)
print(numbers)

print("Even numbers:")
numbers_odd = filter(lambda x: x % 2 == 0, numbers)
print(list(numbers_odd))

print("Odd numbers:")
numbers_even = filter(lambda x: x % 2 != 0, numbers)
print(list(numbers_even))

print('List emails:')
emails = ['marciolaexisolate@gmail', 'marciolaexisolate@hotmail', 'marciolaexisolate@outlook']
provider_google = filter(lambda email: 'gmail' in email, emails )
print(list(provider_google))