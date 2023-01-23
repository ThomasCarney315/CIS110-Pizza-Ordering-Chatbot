print('Hello, my name is Alex your virtual assistant. I will help you order a pizza!')
print('I will ask you a few questions. After typing an answer, press enter.')
userName = input('\nEnter your name:  ')
if userName.lower() == 'thomas':
    print(f'\n Greetings {userName} The Creator, my actions are at your fingertips. What is your will?')
else:
    print(f'\nHello, {userName}. Nice to meet you!')
size = input('\nWhat size pizza would you like? Enter small, medium, or large:  ')
flavor = input('\nEnter the flavor of pizza you want:  ')
crustType = input('\n What type of crust would you like:  ')
quantity = input('\nHow many of these do you want to order? Enter a numeric value:  ')
quantity = int(quantity)
method = input('\nIs this for carry out or delivery:  ')
salesTax = 1.1
if size.lower() == 'small':
    pizzaCost = 8.99
elif size.lower() == 'medium':
    pizzaCost = 14.99
elif size.lower() == 'large':
    pizzaCost = 17.99
if method.lower() == 'delivery':
    deliveryFee = 5
else:
    deliveryFee = 0
total = (pizzaCost * quantity) * salesTax + deliveryFee
print('-' * 10)
print(f'Thank you, {userName}, for your order.')
print(f'Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.')
if total >= 50:
    print('\nCongrats! You get 10$ off your next order!')
else:
    print('\nAny order of 50$ or more will reward you with 10$ off your next order.')
print('-' * 10)