# Task 1
print("პერსონალური მონაცემები")

name = "Beka"          
age = 34               
height = 1.75          
is_student = False     

print(f"მომხმარებლის მონაცემები:")
print(f"სახელი: {name}")
print(f"ასაკი: {age} წლის")
print(f"სიმაღლე: {height} მეტრი")
print(f"სტუდენტია: {is_student}")

print("-------------------------------")

# Task 2
print("საბანკო ტრანზაქცია")

subtotal = 125.0      # ფასი
tax_rate = 0.15       # პროცენტი
discount = 10.0       # ფასდაკლება
people = 7            # მყიდველის რაოენობა


tax_amount = subtotal * tax_rate

total_discount = subtotal + tax_amount

final_total = total_discount - discount

amount_per_person = final_total / people

print(f"ჯამი: ${subtotal:.2f}")
print(f"მომსახურება (15%): ${tax_amount:.2f}")
print(f"ფასდაკლება: -${discount:.2f}")
print(f"საბოლოო გაასახდელი: ${final_total:.2f}")
print(f"ერთ ადამიანზე: ${amount_per_person:.2f}")

print("-------------------------------")

# Task 3
print("ტემპერატურის შედარება")

current_temp = 25
target_temp = 20

print(f"არსებული ტემპერატურა: {current_temp}°C | სავარაუდოტემპერატურა: {target_temp}°C")

print(f"ტოლია თუ არა არსებული ტემპერატურა? (==)  {current_temp == target_temp}")
print(f"ტოლია თუ არა არსებული ტემპერატურა? (!=)  {current_temp != target_temp}")
print(f"უფრო თბილია თუ არა? (>)                   {current_temp > target_temp}")
print(f"უფრო ცივია თუ არა? (<)                     {current_temp < target_temp}")
print(f"ტემპერატურა იგივეა თუ უფრო ცივი? (>=)      {current_temp >= target_temp}")
print(f"ტემპერატურა იგივეა თუ უფრო თბილი? (<=)    {current_temp <= target_temp}")

print("-------------------------------")

# Task 4
print("ტიპების შემოწმება")

version = "v2.5.0"       
build_number = 15
success_rate = 98.5       
is_automated = False  

print(f"მნიშვნელობა: {version} | {type(version)}")
print(f"მნიშვნელობა: {build_number} | {type(build_number)}")
print(f"მნიშვნელობა: {success_rate} | {type(success_rate)}")
print(f"მნიშვნელობა: {is_automated} | {type(is_automated)}")

print("-------------------------------")
# Task 5
print("მათემატიკური ოპერაციები")

num1 = 25
num2 = 7

print(f"რიცხვები: {num1} და {num2}")

print(f"მიმატება (+):         {num1 + num2}")   
print(f"გამოკლება (-):        {num1 - num2}")    
print(f"გამრავლება (*):       {num1 * num2}")    
print(f"გაყოფა (/):           {num1 / num2}")  
print(f"მთელი გაყოფა (//):    {num1 // num2}") 
print(f"ნაშთი გაყოფიდან (%):  {num1 % num2}")
print(f"ხარისხში აყვანა (**):  {num1 ** num2}")