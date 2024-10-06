name = input("What is your name? ")
name_file = open('name.txt', 'w')
name_file.write(name)
name_file.close()

name_file = open('name.txt', 'r')
name = name_file.read()
name_file.close()
print("Hello Mr or Miss " + name + "!")

numbers = open('numbers.txt', 'r')
first_number = int(numbers.readline())
second_number = int(numbers.readline())
sum_of_first_two = first_number + second_number
print("The sum of the first two numbers is: " + int(sum_of_first_two))
numbers.close()

numbers = open('numbers.txt', 'r')
total = 0
for line in numbers:
    total += int(line)
numbers.close()
print("The total is: " + str(total))
