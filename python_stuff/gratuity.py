__author__ = 'student'



def grand_total_for_each():
    subtotal = raw_input("What is the subtotal?")
    party_of = raw_input("How many in your group?")
    whatever = (int(subtotal) + (int(subtotal) * .2)) / int(party_of)
    print whatever

grand_total_for_each()
