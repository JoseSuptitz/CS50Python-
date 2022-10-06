from validators import email

user_input = input("What's your email address? ")

if not email(user_input):
    print('Invalid')
else:
    print('Valid')