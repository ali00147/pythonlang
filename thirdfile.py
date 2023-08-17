def create_user_account():
    uniqueChars = "$%&*@!.,|:"
    numbers = "123456789"
    chars = "abcdefghijklmnopqrstuvwxyz"
    
    while True:
        user_name = input("Please choose a username (must have six characters, including at least one number and one letter): ")
        
        if len(user_name) != 6:
            print("Username must have exactly six characters.")
            continue
        
        has_number = any(char.isdigit() for char in user_name)
        has_char = any(char.isalpha() for char in user_name)
        
        if not (has_number and has_char):
            print("Username must contain at least one number and one letter.")
            continue
        
        break

    while True:
        password = input("Please enter a password (must have at least one unique character: $%&*@!.,|:): ")

        if not any(char in uniqueChars for char in password):
            print("Password must contain at least one unique character: $%&*@!.,|:")
            continue

        break

    print("Success, you have created your account.")

    return user_name, password

def storing_customers_info():
    customers = []

    while True:
        user_name, password = create_user_account()

        customer_profile = {}
        customer_profile["Name"] = input("Enter your Name:\n")
        customer_profile["Age"] = int(input("Enter your Age:\n"))
        customer_profile["Address"] = input("Enter your Current Address:\n")
        customer_profile["City"] = input("Enter the City:\n")
        customer_profile["State"] = input("Enter The State:\n")
        customer_profile["Email"] = input("Enter your Email Address:\n")
        customer_profile["Phone"] = input("Enter your Phone number:\n")
        
        customers.append((user_name, password, customer_profile))

        user_response = input("Would you like to continue entering data? (yes/no): ")
        if (user_response.lower() == "no") or (user_response.upper()) or (user_response=="n") or (user_response=="N"):
            print("Thank you, see you soon!")
            break

    for user_name, password, customer in customers:
        print("User Account:")
        print(f'Username: {user_name}\nPassword: {password}')
        for key, value in customer.items():
            print(f"{key}: {value}")
        print("-" * 20)

    return customers

if __name__ == "__main__":
    storing_customers_info()
