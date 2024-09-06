def print_numbers(*args):
    numbers=[]
    for num in args:
        numbers.append(num)
        print(sum(numbers))

print_numbers(1,5,20)