user_credentials = {
    "john_doe" : "pass#123",
    "jane_smith" : "abc@123",
    "bob_johns" : "passw0rd"
}


def login(usr, pas): # usr si pas variabile locare, primite din afara ca argumente.
    """
    Functie care primeste ca prametrii date de logare si logheaza userul.

    :param usr: str, reprezinta numele de utilizator
    :param pas: str, reprezinta parola
    :return:
    """

    if usr in user_credentials and pas == user_credentials[usr]:
        print("Login successful!")
    elif usr not in user_credentials:
        print("User not found")
    elif pas != user_credentials[usr]:
        print("Password mismatch")


def register():
    new_username = input("New Username:")

    if new_username in user_credentials:
        print("User already exists!")
    else:
        new_password = input("New Password:")
        if new_username == new_password:
            print("Password cannot be the same as username")
        else:
            user_credentials[new_username] = new_password

print("1.Logare")
print("2.Inregistrare")
print("3.Iesire")

choice = int(input("Alege o optiune:"))

while choice != 3:
    if choice == 1:
        username = input("Username:") #variabila globala, toate functiile o recunosc.
        password = input("Password:")
        login(username, password)

    if choice == 2:
        register()
       #login()

    choice = int(input("Alege o optiune:"))
