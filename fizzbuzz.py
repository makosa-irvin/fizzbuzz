#write program that prints the numbers 1 to TBD but prints 'fizz' in multiples of 3, 'buzz' in multiples of 5 and
#'fizzbuzz' in multiples of 3 and 5

def fizz_buzz (num):
    fizzbuzz_string = ''
    for i in range(1, num + 1):
        if i % 3 ==0 and i % 5 == 0:
            fizzbuzz_string += 'fizzbuzz '
        elif i % 3 == 0:
            fizzbuzz_string += 'fizz '

        elif i % 5 == 0:
            fizzbuzz_string += 'buzz '
        else :
            fizzbuzz_string += str(i) + ' '
    print(fizzbuzz_string)

#user inputs number
stop_num = int(input('Enter a number >'))
fizz_buzz(stop_num)