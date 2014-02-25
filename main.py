import convert
from data import get_reachable_stops_from_name
from draw import draw_circle, save_kml

def draw_reachable_stops_from_name(name, start_rad, end_rad):
    reachable_stops = get_reachable_stops_from_name(name, start_rad)
    for stop in reachable_stops:
        lat, lon = convert.OSGB36toWGS84(stop.x, stop.y)
        draw_circle(stop.name, lat, lon, end_rad)
    save_kml()

if __name__ == '__main__':
    import sys
    _, name, start_rad, end_rad = sys.argv
    start_rad, end_rad = float(start_rad), float(end_rad)
    draw_reachable_stops_from_name(name, start_rad, end_rad)
