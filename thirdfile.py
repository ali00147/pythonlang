
profile={"name":"NA","age":"NA",
                      "address":"NA","email":"NA","phone":"NA"}
userinput={"name":"Maslah","age":15,
               "address":"Ohio","email":"mas@gmail.com",
            "phone":"666-668-2555"}

profile|=userinput
print(profile)
    
def storing_customers_info():
    users_input=[]
    customer_profile={}
    
    result_of_data_entered={}
    while True:
        
        customer_profile["Name"]=input("Enter your Name:\n")
        customer_profile["Age"]=input("Enter your Age:\n")
        customer_profile["Address"]=input("Enter your Current Address:\n")
        customer_profile["City"]=input("Enter the City:\n")
        customer_profile["State"]=input("Enter The State:\n")
        customer_profile["Email"]=input("Enter your Email Address:\n")
        customer_profile["Phone"]=input("Enter your Phone number:\n")

        users_input.append(customer_profile)

        user_response= input("Would like to contiune entering data")
        if user_response =="no":
            print("Thank you, see you soon!",customer_profile)
            break
        else:
            continue
    print(customer_profile)
    return customer_profile

if __name__=="__main__":
    storing_customers_info()
