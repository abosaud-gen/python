number = int(input('Enter a "three digit" number: '))
copy = number 
total_sum = 0 

while copy:
    remainder = copy % 10 
    total_sum  += (remainder ** 3)
    copy //= 10 

if total_sum == number:
    print("ARMSTRONG NUMBER")
else:
    print("NOT AN ARMSTRONG NUMBER")
