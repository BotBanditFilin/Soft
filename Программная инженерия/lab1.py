import folium
from folium import Element

stadiums_location = {
    "Лужники": "37.554191,55.715551",
    "Спартак": "37.440262,55.818015",
    "Динамо": "37.559809,55.791540"
}

m = folium.Map(location=[55.7558, 37.6173], zoom_start=11)

for name, coord in stadiums_location.items():
    lat, lon = map(float, coord.split(","))
    folium.Marker([lon, lat], tooltip=name).add_to(m)

custom_css = """
    .leaflet-control-attribution {
        display: none !important;
    }
"""
css_element = Element(f'<style>{custom_css}</style>')

m.get_root().html.add_child(css_element)

m.save("map1.html")
