print("-"*38)
print("-"*15 + " TASK 1 " + "-"*15)# ==============================
# Task 1: Find the smallest number
# ==============================
# Write a function smallest(numbers) that returns the smallest number in a
# list. You are NOT allowed to use min().
#
# Test cases:
#   smallest([4, 2, 9, 1, 7])   -> 1
#   smallest([-3, -10, -1, -7]) -> -10
#   smallest([5])               -> 5

# 1. UNDERSTAND:
# 2. PLAN (pseudocode):
# 3. CODE:
# 4. TEST:

# უნდა დავწეროთ ფუნქცია, რომელიც იპოვნის ყველაზე პატარა რიცვს
# თუ ლისტი ცარიელია დავაბრუნოთ None
# ავიღოთ ლისტის პირველი მნიშცნელობა და შევადაროთ მომდევნოებს
# თუ ლისტის პირველი წევრი იქნება ყველაზე პატარა დავტოვოთ ან განვაახლოთ პატარათი


def smallest(numbers):
    if len(numbers) == 0:
        return None
    
    smallest_num = numbers[0]

    for num in numbers[1:]:
        if num < smallest_num:
            smallest_num = num
    
    return smallest_num

print(smallest([4, 2, 9, 1, 7]))
print(smallest([-3, -10, -1, -7]))
print(smallest([5]))


print(smallest([]))

print("-"*38)
print("-"*15 + " TASK 2 " + "-"*15)
# ==============================
# Task 2: Count even numbers
# ==============================
# Write a function count_evens(numbers) that returns how many numbers in the
# list are even.
#
# Test cases:
#   count_evens([1, 2, 3, 4, 5, 6]) -> 3
#   count_evens([1, 3, 5, 7])       -> 0
#   count_evens([])                 -> 0

# 1. UNDERSTAND:
# 2. PLAN (pseudocode):
# 3. CODE:
# 4. TEST:

# უნდა დავწეროთ ფუნქცია, რომელიც ლისტში დაითვლის რამდენი ლუწი რიცხვია


# counter = 0

# for num in numbers:
#     if num % 2 == 0:
#         counter +=1
    

def counter_evens(numbers):
    counter = 0

    for  num in numbers:
        if num % 2 == 0:
            counter += 1

    return counter

print(counter_evens([1, 2, 3, 4, 5, 6]))
print(counter_evens([1, 3, 5, 7]))
print(counter_evens([]))

print(counter_evens([2, 4, 6, 8]))


print("-"*38)
print("-"*15 + " TASK 3 " + "-"*15)

# Task 3: Reverse a list
# ==============================
# Write a function reverse_list(items) that returns a new list with the
# elements in reverse order. You are NOT allowed to use .reverse() or the
# slicing trick [::-1].
#
# Test cases:
#   reverse_list([1, 2, 3, 4]) -> [4, 3, 2, 1]
#   reverse_list(["a", "b"])   -> ["b", "a"]
#   reverse_list([])           -> []

# 1. UNDERSTAND:
# 2. PLAN (pseudocode):
# 3. CODE:
# 4. TEST:

# უნდა დავწეროთ ფუნქცია, რომელიც დააბრუნებს ლისტის შებრუნებულ ლისტს

def reverse_list(items):
    reverse_items = []

    for item in range(items):
        reverse_items.append(items[item])

    return reverse_items

print(reverse_list([1, 2, 3, 4]))   # [4, 3, 2, 1]
print(reverse_list(["a", "b"]))     # ["b", "a"]
print(reverse_list([]))             # []


print("-"*38)
print("-"*15 + " TASK 4 " + "-"*15)

# Task 4: Does the list contain a value?
# ==============================
# Write a function contains(numbers, target) that returns True if `target`
# appears anywhere in the list, and False otherwise. You are NOT allowed to
# use the `in` keyword for this task - the point is to design the search
# yourself.
#
# Test cases:
#   contains([3, 7, 2, 8], 7) -> True
#   contains([3, 7, 2, 8], 5) -> False
#   contains([], 1)           -> False

# 1. UNDERSTAND:
# 2. PLAN (pseudocode):
# 3. CODE:
# 4. TEST:

# უნდა დავწეროთ ფუნქცია, რომელიც
# დააბრუნებს True-ს თუ ლისტში არის ჩვენს მიერჩაწერილი ციფრი
# ისე, რომ არ გამოვიყენნოთ in  ოპრტატორი

# ავიღოთ ჩვენი ციფრი და შევადაროთ მასივის თიტოეულ წევს 
# თუ რომელიმე მცელობა უდრის დავაბრუნოთ True

def contains(numbers, target):
    for num in numbers:
        if num == target:
            return True
    return False

print(contains([3, 7, 2, 8], 7))
print(contains([3, 7, 2, 8], 5))
print(contains([], 1))

print(contains([3, 3, 3], 3))


print("-"*38)
print("-"*15 + " TASK 5 " + "-"*15)

# Task 5: Count a letter in a string
# ==============================
# Write a function count_letter(text, letter) that returns how many times
# `letter` appears in `text`. Treat uppercase and lowercase as the same
# letter (so "A" and "a" both count).
#
# Test cases:
#   count_letter("banana", "a")      -> 3
#   count_letter("Mississippi", "s") -> 4
#   count_letter("Hello", "z")       -> 0

# 1. UNDERSTAND:
# 2. PLAN (pseudocode):
# 3. CODE:
# 4. TEST:

# დავწეროთ ფუნქცია, რომელიც
# სიტყვიდან დაითვლის რამდენჯერ გვხვდება ჩვნეს მიერ არჩეული ასო
# არ აქვს მნიშვნელობა იქნება დიდი თუ პატარა

# counter = 0

# text- ი გადავიყვანოთ lower

# ციკლით მოვძებნოთ ასო თუა სიტყვაში
# თუ არის counter + 1

def count_letter(text, letter):
    count = 0

    text = text.lower()
    letter = letter.lower()

    for char in text:
        if char == letter:
            count += 1

    return count

print(count_letter("banana", a))
print(count_letter("Mississippi", "s"))
print(count_letter("Hello", "z"))

print(count_letter("BaNANa", "A"))