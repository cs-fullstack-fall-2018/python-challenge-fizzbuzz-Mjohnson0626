# import os
#
# os.system('clear')

my_file = open('fizzbuzz.txt', 'w+')

for num in range(1, int(input('chose the max'))):
    if num % 3 == 0 and num %5 == 0:
        my_file.write(str(num)+ ' FizzBuzz \n')
        print(num,'FizzBuzz')
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)