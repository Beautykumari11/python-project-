import csv
import requests

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

def get_coordinates(city, key):
    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={key}"
    
    try:
        resp = requests.get(geocoding_url)
        if resp.status_code != 200:
            return None, f"Can't get coordinates. Status code: {resp.status_code}"
        
        data = resp.json()
        if not data:
            return None, f"City {city} not found."
        
        lat = data[0]['lat']
        lon = data[0]['lon']
        return (lat, lon), None
    except requests.exceptions.RequestException as e:
        return None, f"Error making request for coordinates: {e}"

def get_air(city):
    key = 'f26d7a75d08eeaddedd5787910821326'  # Replace with your new OpenWeatherMap API key
    
    coords, error = get_coordinates(city, key)
    if error:
        return error
    
    lat, lon = coords
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}"
    
    print(f"Requesting URL: {url}")  # Debug print
    
    try:
        resp = requests.get(url)
        print(f"Response status code: {resp.status_code}")  # Debug print
        print(f"Response content: {resp.text}")  # Debug print
        
        if resp.status_code != 200:
            return f"Can't get data. Status code: {resp.status_code}"
        
        data = resp.json()
        aqi = data['list'][0]['main']['aqi']
        
        levels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
        
        return f"Air in {city}: AQI {aqi} - {levels.get(aqi, 'Unknown')}"
    except requests.exceptions.RequestException as e:
        return f"Error making request: {e}"
    except KeyError as e:
        return f"Error parsing response: {e}. Response data: {data}"
    except Exception as e:
        return f"Unexpected error: {e}"

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
