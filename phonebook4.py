#test record
phonebook = {'holly': ['grant', '0987987']}

#to-do: clean up the prompt format (tabbing, e.g.)
#to-do error handling

intention = input ('what would you like to do? Type 1 for search, 2 for add, 3 for remove, or 4 for update')
'1. search'
'2. add'
'3. remove'
'4. exit'

#to-do handle user input errors
if intention == 1:
    who_are_you_looking_for = raw_input('search by last name').lower()
    print(phonebook[who_are_you_looking_for])

if intention == 2:
    city = raw_input('enter the new key as city to be added').lower()
    value = raw_input("enter the value").lower()
    ph = {city:value}
    phonebook.update (ph)
    print phonebook

#error handling
if intention == 3:
    who_do_you_want_to_remove = raw_input ('search by last name or city').lower()
    removed_person= phonebook.pop(who_do_you_want_to_remove)
    print(removed_person)
    print phonebook

if intention == 4:
    print ("control_c to exit")

