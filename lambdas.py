extract_prov_imail = lambda email: email.split('@')[1]
email = 'marciolaexisolate@gmail'
print(extract_prov_imail(email))

number_odd = lambda number: True if number % 2 == 0 else False
numbers =range(1,10)
for number in numbers:
    if number_odd(number) == True:
        print(f'{number} is odd')