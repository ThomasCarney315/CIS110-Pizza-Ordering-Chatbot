import time, sys, colorama, winsound

from colorama import init, Fore, Back, Style
# colorama.init(autoreset=True)

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.025)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

r = Fore.RESET
re = Fore.RED
gr = Fore.GREEN
bl = Fore.BLUE
wh = Fore.WHITE
ye = Fore.YELLOW
ma = Fore.MAGENTA
cy = Fore.CYAN

typingPrint(cy + 'Hello, my name is Alex your virtual assistant. I will help you order a pizza!''I will ask you a few questions. After typing an answer, press' + r + ' enter.\n')
userName = typingInput('\nEnter your name:  ')
while len(userName) == 0:
    winsound.PlaySound("chord.wav", winsound.SND_ALIAS)
    userName = input(ye +'You must have a name! To continue, please enter your name:  ' + r)
if userName.lower() == 'thomas':
    typingPrint(gr + f'\n Greetings {userName} The Creator, my actions are at your fingertips. What is your will?' + r)
else:
    typingPrint(cy + f'\nHello, {userName}. Nice to meet you!' + r)
size = typingInput(cy + '\nWhat size pizza would you like? Enter small, medium, or large:  ' + r)
while size.lower() not in ['small', 'medium', 'large']:
    winsound.PlaySound("chord.wav", winsound.SND_ALIAS)
    size = input(ye + '\nPlease choose small, medium, or large:  ' + r)
flavor = typingInput(cy + '\nEnter the flavor of pizza you want:  ' + r)
while len(flavor) == 0:
    winsound.PlaySound("chord.wav", winsound.SND_ALIAS)
    flavor = input(ye + '\nDon\'t you like flavor? Please pick a flavor:  ' + r)
crustType = typingInput(cy +'\nWhat type of crust would you like:  ' + r)
while len(crustType) == 0:
    winsound.PlaySound("chord.wav", winsound.SND_ALIAS)
    crustType = input(ye + '\nPlease pick a crust type:  ' + r)
quantity = typingInput(cy + '\nHow many of these do you want to order? Enter a numeric value:  ' + r)
while not quantity.isdigit():
    winsound.PlaySound("chord.wav", winsound.SND_ALIAS)
    quantity = input(ye +'\nThat\'s not a number. Please enter a number:  ' + r)
quantity = int(quantity)
method = typingInput(cy + '\nIs this for carry out or delivery:  ' + r)
while method.lower() not in ['carry out', 'delivery']:
    winsound.PlaySound("chord.wav", winsound.SND_ALIAS)
    method = input(ye + '\nPlease enter carry out or delivery:  ' + r)
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
typingPrint(cy + f'Thank you, {userName}, for your order.' + r)
typingPrint(cy + f'Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.' + r)
if total >= 50:
    winsound.PlaySound("tada.wav", winsound.SND_ALIAS)
    typingPrint(gr +'\nCongrats! You get 10$ off your next order!\n' + r)
else:
    typingPrint(re + '\nAny order of 50$ or more will reward you with 10$ off your next order.\n' + r)
print('-' * 10)
k=input('\npress close to exit') 