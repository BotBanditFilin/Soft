import requests

def find_pharm(addr):
    geo_key = 'a1355d6f-dd8c-4213-87ae-e306ba7ab76a'
    search_key = 'faff8dce-2eef-494b-b502-283981bedc45'

    try:
        geo_res = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={geo_key}&format=json&geocode={addr}')
        geo_data = geo_res.json()

        coords = geo_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        lon, lat = map(float, coords.split())

        pharm_res = requests.get(f'https://search-maps.yandex.ru/v1/?apikey={search_key}&text=аптека&ll={lon},{lat}&type=biz&lang=ru_RU&results=1')
        pharm_data = pharm_res.json()

        pharm = pharm_data['features'][0]
        name = pharm['properties']['name']
        addr = pharm['properties']['CompanyMetaData']['address']

        return name, addr
    except Exception as e:
        return "Ошибка при поиске аптеки:", str(e)

if __name__ == "__main__":
    addr = input("Введите адрес: ")
    result = find_pharm(addr)
    print("Ближайшая аптека:")
    print("Название:", result[0])
    print("Адрес:", result[1])
