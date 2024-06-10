import math

def dist(a, b):
    factor = 111000
    lon1, lat1 = a
    lon2, lat2 = b

    rad_lat = math.radians((lat1 + lat2) / 2.0)
    lat_factor = math.cos(rad_lat)

    dx = abs(lon1 - lon2) * factor * lat_factor
    dy = abs(lat1 - lat2) * factor

    d = math.sqrt(dx**2 + dy**2)

    return d

h_lat, h_lon = map(float, input("Введите широту и долготу вашего дома через пробел: ").split())
u_lat, u_lon = map(float, input("Введите широту и долготу вашего университета через пробел: ").split())

d = dist((h_lon, h_lat), (u_lon, u_lat))
print(f"Расстояние между вашим домом и университетом примерно {d:.2f} метров.")
