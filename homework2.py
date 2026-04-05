print("-"*15 + "Task 1" + "-"*15)

name = input("შეიყვანეთ თქვენი სახელი: ")

print(f"გამარჯობა, {name.upper()}")
print(f"გამარჯობა, {name.lower()}")
print(f"გამარჯობა, {name.title()}")

print("-"*30)

print("-"*15 + "Task 2" + "-"*15)

sentence = "  the quick brown fox jumps over the lazy dog  "

print(f"Stripped: '{sentence.strip()}'")

print(f"რამდენი 'o' ასოა?: {sentence.count('o')}")

print(f"ჩანაცვლება: {sentence.replace('fox', 'cat')}")

words = sentence.split()
print(f"პირველი 3 სიტყვა: {words[0:3]}")

print("-"*30)

print("-"*15 + "Task 3" + "-"*15)

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")
elif age < 13:
    print("You are a child.")
elif age <= 17:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")

print("-"*30)

print("-"*15 + "Task 4" + "-"*15)

username = input("Enter a username: ")  
password = input("Enter a password: ")


if username == "admin" and password == "secret":
    print("Welcome, Admin!")
elif username == "admin" and password != "secret":
    print("Incorrect password.")
else:
    print("User not found.")


print("-"*30)

print("-"*15 + "Task 5" + "-"*15)

age = int(input("ჩაწერეთ თქვენი ასაკი: "))
student_status = input("ხართ თუ არა სტუდენტი? (yes/no): ").strip().lower()

if age < 12:
    price = 5
elif student_status == "yes":
    price = 8
elif age >= 65:
    price = 10
else:
    price = 15

print(f"Ticket price: ${price}")
