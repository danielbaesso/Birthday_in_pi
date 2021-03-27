# First you need download this txt: https://github.com/ehmatthes/pcc/blob/master/chapter_10/pi_million_digits.txt

filename = "./pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

    pi_string = ""

    for line in lines:
        pi_string += line.strip()

    b_day = input("Enter your birthday in the form mmddaa: ")
    if b_day in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appears in the first million digits of pi.")
