num = 25
counter = 2

while counter < num:
    if num%counter == 0:
        print(f'{num} it is not prime number')
        break
    counter += 1
else:
    print(f'{num} is a prime number')

# to check if a number is prime or not.
