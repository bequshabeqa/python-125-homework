from glob import translate
from turtle import st


print("-"*15 + " TASK 1 " + "-"*15)

grades = {
    "Beqa": 58,
    "Giorgi": 67,
    "Ani": 92,
    "Mari": 91,
    "Xatuna": 78
}

total = 0
student = {
    "name": "",
    "grade": 0
}
for name, grade in grades.items():
    print(name, grade)
    if student["grade"] < grade:
        student["name"] = name
        student["grade"] = grade

average = sum(grades.values()) / len(grades)
print(f"avg: {average}")
print(student["name"])



print("-"*38)
print("-"*15 + " TASK 2 " + "-"*15)

text = "Hello World"

def count_letters(text):
    counts = {}
    
    for char in text.lower():
        if char != " ":         
            counts[char] = counts.get(char, 0) + 1
            
    return counts

print(count_letters(text))

print("-"*38)
print("-"*15 + " TASK 3 " + "-"*15)

def merge_lists(list1, list2):
    merged = list1.copy()  
    
    for item, quantity in list2.items():
        if item in merged:
            merged[item] += quantity
        else:
            merged[item] = quantity
            
    return merged

list1 = {"milk": 2, "bread": 1, "eggs": 12}
list2 = {"bread": 2, "cheese": 1, "milk": 1}

print(merge_lists(list1, list2))

print("-"*38)
print("-"*15 + " TASK 4 " + "-"*15)

contacts = []


def add_contact(contacts, name, phone, email): 
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

def find_by_name(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
        
    return None

def all_emails(contacts):
    emails = []
    for contact in contacts:
        emails.append(contact["email"])
    return emails


add_contact(contacts, name= "Beqa", phone= 7, email="b@gmail.de")
add_contact(contacts, name="Giga", phone= 7, email="giga@mail.de")



print(contacts)

print(find_by_name(contacts, name="Beqa"))
print(find_by_name(contacts, name="Anna"))

print(all_emails(contacts))


print("-"*38)
print("-"*15 + " TASK 5 " + "-"*15)

class_a = ["Inception", "Matrix", "Interstellar", "Joker", "Matrix"]
class_b = ["Matrix", "Titanic", "Joker", "Avatar", "Titanic"]

class_a = set(class_a)
class_b = set(class_b)

print(class_a & class_b)
print(class_a.symmetric_difference(class_b))
print(class_a | class_b)


print("-"*38)
print("-"*15 + " TASK 6 " + "-"*15)

translator = {
    "hello": "გამარჯობა",
    "cat": "კატა",
    "dog": "ძაღლი",
    "how": "როგორ",
    "are": "ხარ",
    "you": "შენ"

}

sentence = "hello how are you"

def translate(sentence):
    translated = []
    for word in sentence.split(" "):
        # print(translator[word])
        translated.append(translator.get(word, word))

    return " ".join(translated)

print(translate(sentence))
    