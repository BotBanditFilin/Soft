import requests

def find_dist(addr):
    key = 'a1355d6f-dd8c-4213-87ae-e306ba7ab76a'

    try:
        geo_resp = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&format=json&geocode={addr}')
        geo_data = geo_resp.json()

        coords = geo_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        long, lat = map(float, coords.split())

        dist_resp = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&format=json&geocode={long},{lat}&kind=district')
        dist_data = dist_resp.json()

        dist = dist_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']

        return dist
    except Exception as e:
        return "Ошибка:", str(e)

if __name__ == "__main__":
    addr = input("Введите адрес: ")
    res = find_dist(addr)
    print("Район:", res)
