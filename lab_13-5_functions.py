#used a function from last lab then looked online for different functions
def count_letters(word):
    letter_counts = {}
    for letter in word:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def max_in_list(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def sum_of_list(numbers):
    total = 0
    index = 0
    while index < len(numbers):
        total += numbers[index]
        index += 1
    return total

def list_details(names):
    for index, name in enumerate(names):
        print(f"{index + 1}: {name}")
    return len(names)

def multiply_numbers(a, b):
    return int(a) * int(b)

def get_lower_case(word):
    return word.lower()

def get_input_sum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 + num2

def sort_list(my_list):
    return sorted(my_list)

def reverse_string(string):
    return ''.join(reversed(string))

def calculate_length(word):
    '    return len(word)

