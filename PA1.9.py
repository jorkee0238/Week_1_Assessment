name=input('Please enter your name: ')
studentID=input('Please enter your student ID: ')
num1=int(input('Please enter a whole number: '))
num2=int(input('Please enter a second whole number: '))
add = num1 + num2
minus = num2 - num1
multiplication = num1 * num2

print(f" {num1} + {num2} = {add:,.2f}")
print(f" {num2} - {num1} = {minus:,.2f}")
print(f" {num1} * {num2} = {multiplication:,.2f}")

if num1>num2:
    print(f'Number 1 is larger than number 2.')
elif num1<num2:
    print(f'Number 2 is larger than number .')
print(f'{name}')
print (f'{studentID}')
