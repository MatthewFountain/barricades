#test record
phonebook = {'jones': ['tom', '0987987']}

#to-do: clean up the prompt format (tabbing, e.g.)
#to-do error handling

intention = input ('what would you like to do? Type 1 for search, 2 for add, 3 for remove, or 4 for exit:')
'1. search'
'2. add'
'3. remove'
'4. exit'

#to-do handle user input errors
if intention == 1:
    who_are_you_looking_for = raw_input('search by last name').lower()
    print(phonebook[who_are_you_looking_for])

#get new data from the User
if intention == 2:
    firstname=raw_input("Enter ur firstname:")
    lastname=raw_input("Enter ur Lastname:")
    phonenumber=raw_input("Enter ur Phonenumber:")
    newentry = {firstname: [lastname,phonenumber]}
    phonebook.update(newentry) 
    print phonebook

#error handling
if intention == 3:
    who_do_you_want_to_remove = raw_input ('search by last name').lower()
    removed_person= phonebook.pop(who_do_you_want_to_remove)
    print(removed_person)
    print phonebook

#Quit the program
if intention == 4:
    print ("control_c to exit")

