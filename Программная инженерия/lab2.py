import folium
from geopy.distance import geodesic
from folium import Element

points = [
    (55.715551, 37.554191),
    (55.818015, 37.440262),
    (55.791540, 37.559809),
    (55.751244, 37.618423) 
]

def calculate_path_length(points):
    length = 0
    for i in range(len(points) - 1):
        length += geodesic(points[i], points[i+1]).kilometers
    return length

path_length = calculate_path_length(points)

m = folium.Map(location=[55.7558, 37.6173], zoom_start=13)

folium.PolyLine(points, color="blue", weight=2.5, opacity=1).add_to(m)

for point in points:
    folium.Marker(location=point).add_to(m)

mid_index = len(points) // 2
mid_point = points[mid_index]
folium.Marker(location=mid_point, popup="Средняя точка пути", icon=folium.Icon(color='red')).add_to(m)

custom_css = """
    .leaflet-control-attribution {
        display: none !important;
    }
"""
css_element = Element(f'<style>{custom_css}</style>')
m.get_root().html.add_child(css_element)

print(f"Длина пути: {path_length:.2f} км")

m.save("path_map.html")
