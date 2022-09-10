"""
What this file will do:- It will ask user about their firstname, lastname and birthyear and generate a random username for their social media profile

Input:
1 - firstname
2 - lastname
3- birthyear

Output:
random generated username basis on firstname,lastname and birthyear

"""

from random import randint

firstname = input('here we go to generate your random social media username enter firstname:- ')
lastname = input('lastname:- ')
birth_year = input('birth year:- ')

firstname_length = len(firstname)
lastname_length = len(lastname)

random_firstname_length = randint(2,firstname_length)
random_lastname_length = randint(2,lastname_length)

sliced_firstname = firstname[0:random_firstname_length].lower()
sliced_lastname = lastname[0:random_lastname_length].lower()
sliced_birth_year = birth_year[randint(0,1):randint(2,3)]

sliced_user_data = [sliced_firstname,sliced_lastname,sliced_birth_year];

def get_random_value():
    return sliced_user_data[randint(0,2)]

generated_username = ''
count = 0
random_text = '10_29384756'
username_required_length = 10

while len(generated_username) < username_required_length:
    count += 1
    random_string = get_random_value()
    random_string_index = generated_username.rfind(random_string)
    if random_string_index == -1:
        generated_username += random_string
        
    if count == 100:
        generated_username_length = len(generated_username)
        length_difference = username_required_length - generated_username_length
        
        generated_username += random_text[length_difference:length_difference*2]
        
        
# generated_username = generated_username.lower()
print('Hurrey! ' + firstname + " " + lastname + " your social media username is:-   " + generated_username)



