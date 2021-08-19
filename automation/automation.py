import shutil
import re
from faker import Faker

fake = Faker('en_US')

potential_contacts = ""
existing_contacts=""


for i in range(100):

    email = fake.email()
    phone_number = fake.phone_number()
    potential_contacts += " " + email + " "
    potential_contacts += phone_number

    if i % 7 == 0: 
        potential_contacts += " " + email + " "

    if i % 9 == 0: 
        potential_contacts += phone_number


    if i % 5 == 0:
        existing_contacts += email + "\n"
        existing_contacts += phone_number + "\n"


    potential_contacts += "\n"

with open("potential-contacts.txt", "w+") as f:
    f.write(potential_contacts)
    


with open("potential-contacts.txt","r") as f:
 file_content=f.read()

match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file_content)
match=set(match)

with open("email.txt", "w") as f:
    for element in match:
        f.write(element + "\n")

phone = re.findall(r'\d{3}-\d{3}-\d{4}|\d{3}-\d{4}', file_content)

with open("phone.txt", "w") as f:
    for element in phone:
         f.write( element + "\n")

