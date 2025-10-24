import random
import string


# This program creates a password with 4 or more characters and it will have at least
# one uppercase letter, one lowercase letter, one special character, and one number.

list_of_special_characters = ['!', '@', '#', '%', '&', '-', '+', '=']
make_password = "y"

while make_password == "y":
    password_list = []
    number_of_characters = int(input("How many characters?(Must be at least 4): "))

    if number_of_characters < 4:
        while number_of_characters < 4:
            number_of_characters = int(input("Please enter a valid amout of characters (Must be at least 4): "))

    def random_int():
        return str(random.randint(0, 9))
    def random_lowercase():
        return str(random.choice(string.ascii_lowercase))
    def random_uppercase():
        return str(random.choice(string.ascii_uppercase))
    def random_special_character():
        return str(random.choice(list_of_special_characters))
    
    # This function will randomly choose from the 4 above functions to get a random character of any kind.
    def random_character(index):
        random_function_index = 1
        if index <= 4:
            random_function_index = index
        else:
            random_function_index = index % 4 or 4
        
        match random_function_index:
            case 1:
                return random_int()
            case 2: 
                return random_lowercase()
            case 3:
                return random_uppercase()
            case 4: 
                return random_special_character()
            case _:
                print("Error line 33")
                return random_lowercase()
        

    def create_password(num_characters):
        password_list = [random_int(), random_lowercase(), random_uppercase(), random_special_character()]
        while int(len(password_list)) < num_characters:
            password_list.append(random_character(int(len(password_list))))
        random.shuffle(password_list)
        return "".join(password_list)

    password = create_password(number_of_characters)

    

    print(f"Your new password: {password}")

    make_password = input("Make another password? y/n: ")

