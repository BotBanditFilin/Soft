import requests
import random
import webbrowser

def get_coords(city):
    api_key = "a1355d6f-dd8c-4213-87ae-e306ba7ab76a"
    endpoint = "https://geocode-maps.yandex.ru/1.x/"

    params = {
        "apikey": api_key,
        "geocode": city,
        "format": "json"
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    coords = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = map(float, coords.split())

    return lat, lon

cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]

def get_image(lat, lon):
    api_key = "74893686-3544-4633-be2f-5762af43ffe2"
    endpoint = f"https://static-maps.yandex.ru/1.x/?apikey={api_key}"

    map_type = random.choice(["map", "sat"])

    params = {
        "ll": f"{lon},{lat}",
        "size": "250,250",
        "l": "map",
        "z": "12"
    }

    response = requests.get(endpoint, params=params)

    image_url = response.url
    return image_url

def show_image(url):
    webbrowser.open_new_tab(url)

def main():
    while True:
        random.shuffle(cities)
        for city in cities:
            lat, lon = get_coords(city)
            image_url = get_image(lat, lon+0.1)
            show_image(image_url)
            
            input("Угадайте название города: ")
            print(f"Правильный ответ: {city}\n")
            
            input("Нажмите Enter, чтобы продолжить...")
    
if __name__ == "__main__":
    main()
