
numbers = [5, 3, 1, 20, 2]
# for number in numbers:
#     number = int(numbers))
#     numbers.append(number)
print("First number is", numbers[0])
print("Second number is", numbers[-1])
print("The min number is", min(numbers))
print("The max number is", max(numbers))
print("The average number is,", sum(numbers)/len(numbers))

# Other way around

n = [5, 3, 1, 20, 2]

print("There are {0} items".format(len(n)))
print("Maximum is {0}".format(max(n)))
print("Minimum is {0}".format(min(n)))
print("The Average of values is {0} {0}".format (sum(n) / len(n)))