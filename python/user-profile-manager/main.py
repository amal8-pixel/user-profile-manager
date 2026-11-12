name = input("Enter your name: ")
field = input("Enter your specialization: ")


if name.strip() == "":
    print("Please enter your name!")
elif field.strip() == "":
    print("Please enter your specialization!")
else:
    with open("user.txt", "w") as file:
        file.write(name + "\n")
        file.write(field)
    
    
    try:
            
           with open("user.txt", "r") as file: 
            content= file.read()
            print(content)
    
    except FileNotFoundError:
        print("user file not found! ")

    

