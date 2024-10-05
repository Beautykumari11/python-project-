import csv
import requests  
import register

FILE = 'ca2.csv'

def load_users():
    users = {}
    try:
        with open(FILE, 'r') as f:
            for line in f:
                name, pwd = line.strip().split(',')
                users[name] = pwd
    except FileNotFoundError:
        pass
    return users

def save_users(users):
    with open(FILE, 'w') as f:
        for name, pwd in users.items():
            f.write(f"{name},{pwd}\n")

def login():
    users = load_users()
    name = input("Username (or 'exit' to quit): ")
    if name.lower() == 'exit':
        return None
    pwd = input("Password: ")
    if name in users and users[name] == pwd:
        print("Login ok")
        return name
    else:
        print("Wrong login")
        return None

def register():
    users = load_users()
    name = input("New username: ")
    if name in users:
        print("Name taken")
        return
    pwd = input("New password: ")
    users[name] = pwd
    save_users(users)
    print("Registered")

def forget_password():
    users = load_users()
    name = input("Username to reset password: ")
    if name in users:
        pwd = input("New password: ")
        users[name] = pwd
        save_users(users)
        print("Password updated successfully")
    else:
        print("Username not found")

def get_air(city):
    key = 'c6d525e6397e341745a7c1eaa2000f48'
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?q={city}&appid={key}"

    resp = requests.get(url)
    if resp.status_code != 200:
        return "Can't get data"

    data = resp.json()
    aqi = data['list'][0]['main']['aqi']

    levels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}

    return f"Air in {city}: AQI {aqi} - {levels.get(aqi, 'Unknown')}"

def main():
    while True:
        print("\n1. Login\n2. Register\n3. Forget Password\n4. Quit")
        choice = input("Choose: ")

        if choice == '1':
            if login():
                while True:
                    city = input("City for air check (or 'quit' to exit): ")
                    if city.lower() == 'quit':
                        break
                    print(get_air(city))
        elif choice == '2':
            register()
        elif choice == '3':
            forget_password()
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
import csv
import requests  
import register

FILE = 'ca2.csv'

def load_users():
    users = {}
    try:
        with open(FILE, 'r') as f:
            for line in f:
                name, pwd = line.strip().split(',')
                users[name] = pwd
    except FileNotFoundError:
        pass
    return users

def save_users(users):
    with open(FILE, 'w') as f:
        for name, pwd in users.items():
            f.write(f"{name},{pwd}\n")

def login():
    users = load_users()
    name = input("Username (or 'exit' to quit): ")
    if name.lower() == 'exit':
        return None
    pwd = input("Password: ")
    if name in users and users[name] == pwd:
        print("Login ok")
        return name
    else:
        print("Wrong login")
        return None

def register():
    users = load_users()
    name = input("New username: ")
    if name in users:
        print("Name taken")
        return
    pwd = input("New password: ")
    users[name] = pwd
    save_users(users)
    print("Registered")

def forget_password():
    users = load_users()
    name = input("Username to reset password: ")
    if name in users:
        pwd = input("New password: ")
        users[name] = pwd
        save_users(users)
        print("Password updated successfully")
    else:
        print("Username not found")

def get_air(city):
    key = 'c6d525e6397e341745a7c1eaa2000f48'
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?q={city}&appid={key}"

    resp = requests.get(url)
    if resp.status_code != 200:
        return "Can't get data"

    data = resp.json()
    aqi = data['list'][0]['main']['aqi']

    levels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}

    return f"Air in {city}: AQI {aqi} - {levels.get(aqi, 'Unknown')}"

def main():
    while True:
        print("\n1. Login\n2. Register\n3. Forget Password\n4. Quit")
        choice = input("Choose: ")

        if choice == '1':
            if login():
                while True:
                    city = input("City for air check (or 'quit' to exit): ")
                    if city.lower() == 'quit':
                        break
                    print(get_air(city))
        elif choice == '2':
            register()
        elif choice == '3':
            forget_password()
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
