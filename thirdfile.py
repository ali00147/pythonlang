def storing_customers_info():
    customer_profile={"name":"NA","age":"NA",
                      "address":"NA","email":"NA","phone":"NA"}

    userinput={"name":"Maslah","age":15,
               "address":"Ohio","email":"mas@gmail.com",
            "phone":"666-668-2555"}

    customer_profile|=userinput
    print(customer_profile)

    askname=input("Enter your name:\n")
    ask_age= int(input("Enter your age:\n"))
    ask_address= input("Enter your address:\n")
    ask_email= input("Enter your email:\n")
    ask_phone= input("Enter your phone number:\n")

    customer_profile["name"],customer_profile["age"],customer_profile["address"],customer_profile["email"]
    customer_profile["phone"]=askname,ask_age,ask_address,ask_email,ask_phone

    saveresult= customer_profile
    print(saveresult)
    return saveresult

if __name__=="__main__":
    storing_customers_info()
