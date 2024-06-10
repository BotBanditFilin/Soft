def main():
    city_coords = {
        "Москва": 55.7558,
        "Санкт-Петербург": 59.9343,
        "Сочи": 43.6028,
        "Екатеринбург": 56.8389,
        "Владивосток": 43.1155,
        "Уфа": 54.7388,
        "Минск": 53.9045
    }
    
    cities_input = input("Введите список городов через запятую: ")
    cities = [city.strip() for city in cities_input.split(",")]

    southernmost_city = None
    southernmost_lat = float('inf')
    
    for city in cities:
        lat = city_coords.get(city)
        if lat is not None and lat < southernmost_lat:
            southernmost_city = city
            southernmost_lat = lat

    if southernmost_city:
        print(f"Самый южный город: {southernmost_city}")
    else:
        print("Не удалось определить координаты ни одного города")

if __name__ == "__main__":
    main()