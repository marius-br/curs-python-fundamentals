import random

def get_weather(oras):
    conditions=["Inorat", "Insorit", "Ploaie", "Ninsoare"]
    temperature = random.randint(-10, 35)

    data = {
        "city" : oras,
        "temperature" : temperature,
        "condition" : random.choice(conditions)
    }

    return data


def weather_app():
    print("Afla vremea din orasul tau!")

    while True:
        city = input("Introduceti numele orasului sau exit pentru iesire:")

        if city == "exit":
            break

        weather_data = get_weather(city)

        print(f"Pentru orasul: {city}, temperatura este: {weather_data['temperature']} si conditia meteo este: {weather_data['condition']}")

if __name__ == "__main__":
    weather_app()