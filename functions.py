email = 'marcioalexisolate@gmail.com'

def get_email(string)->str:
    return email

print(get_email(email))

def extract_username(email:str):
    user_separed = email.split(sep="@")
    provider_separed = email.split(sep="@")
    return user_separed[0], provider_separed[1]

print(extract_username(email))
