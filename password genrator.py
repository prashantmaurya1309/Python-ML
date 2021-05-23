import random

upper_letter = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lower_letter = upper_letter.lower()
digit = '1234567890'
symbol = '!@#$%^&*(){}:<?>/;[] '

upper, lower, nums, sym = True, True, True, True
all = ''

if upper:
    all+=upper_letter
if lower:
    all+=lower_letter
if nums:
    all+=digit
if sym:
    all+=symbol

lenght = 20
amount = 5

for i in range(amount):
    password = "".join(random.sample(all,lenght))
    print(password)
