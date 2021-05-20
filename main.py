from random import choice



lower_charset = 'abcdefghijklmnopqrstuvwxyz'
upper_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_set = '0123456789'
symbol_set ='!@#$%^&*()'

chars_option = input("Do you want your password to include upper, lower or both? ( use 'u', 'l', 'b' to choose ): ")
nums_option = input('Do you want it to include number? [y/n]: ')
symbols_option = input('Do you want it to include symbols? [y/n]: ')
password_length = int(input('How long do you want your password to be? (maxium: 71 characters): '))

keys = ''
if chars_option == 'u':
    keys += upper_charset
elif chars_option == 'l':
    keys += lower_charset
elif chars_option == 'b':
    keys += lower_charset + upper_charset
if nums_option == 'y':
    keys += num_set
if symbols_option == 'y':
    keys += symbol_set
    
password = []
for _ in range(password_length):
    password.append(choice(keys))


print(f"Here is your password!: {''.join(password)}")
