from itertools import count


print("-"*15 + " TASK 1 " + "-"*15)

movies = ["Spirit", "The Matrix", "The Mask", "Fast & Furiose", "Gladiator"]

print(f"პირველი: {movies[0]}, ბოლო: {movies[-1]}")

movies.append("The Dark Knight")

movies.insert(2, "Spirited Away")

movies.remove("The Mask")  

print("ფილმების ჩამონათვალი:", movies)
print("საერთო ფილმები:", len(movies))

print("-"*38)
print("-"*15 + " TASK 2 " + "-"*15)

numbers = []

for i in range(5):
    num = float(input(f"ჩაწერე რიცხვი: {i+1}: "))
    numbers.append(num)

print("\nჩაწერილი რიცხვები:", numbers)
print("ჯამი:", sum(numbers))
print("საშუალო:", sum(numbers) / len(numbers))
print("უდიდესი:", max(numbers))
print("უმცირესი:", min(numbers))

print("-"*38)
print("-"*15 + " TASK 3 " + "-"*15)

evens = []
odds = []

for num in range(1, 21):
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print("კენტი რიცხვები:", evens)
print("ლუწი რიცხვები:", odds)

print("-"*38)
print("-"*15 + " TASK 4 " + "-"*15)

attempts = 0

while attempts < 3:
    password = input("შეიყვანე პაროლი: ")
    
    if password == "python123":
        print("გილოცავ, პაროლი სწორია!")
        break
    else:
        attempts += 1
        if attempts < 3:
            print(f"არასწორი პაროლი, სცადეთ ხელახლა. ({3 - attempts} დარჩენილი მცდელობა)")
        else:
            print("ანგარიში დაბლოკილია!")


print("-"*38)
print("-"*15 + " TASK 5 " + "-"*15)

num = int(input("შეიყვანეთ რიცხვი: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


print("-"*38)
print("-"*15 + " TASK 6 " + "-"*15)

sentence = input("შეიყვანეთ წინადადება: ").lower()

counts = {"vowels": 0, "consonants": 0}
vowels = "aeiou"
vowel_count = 0 

for char in sentence:
    if char in vowels:
        vowel_count += 1
    else:
        counts["consonants"] += 1
counts["vowels"] = vowel_count

print(f"ხმოვნების რაოდენობა: {counts['vowels']}")
print(f"თანხმოების რაოდენობა: {counts['consonants']}")