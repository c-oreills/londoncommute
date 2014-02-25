#!/usr/bin/env python

import convert
from data import get_reachable_stops_from_name
from draw import draw_circle, save_kml

def draw_reachable_stops_from_name(name, rad):
    reachable_stops = get_reachable_stops_from_name(name, rad)
    lat_rad, lon_rad = None, None
    for stop in reachable_stops:
        if not (lat_rad and lon_rad):
            # Work out radius in latitudinal/longitudinal degrees for this
            # general area
            lat_rad, lon_rad = calculate_lat_lon_rads(stop, rad)
        lat, lon = convert.OSGB36toWGS84(stop.x, stop.y)
        draw_circle(stop.name, lat, lon, lat_rad, lon_rad)
    save_kml()

def calculate_lat_lon_rads(stop, rad):
    lat_rad, lon_rad = convert.OSGB36toWGS84(stop.x, stop.y)
    lat_rad_d, lon_rad_d = convert.OSGB36toWGS84(stop.x-rad, stop.y-rad)
    lat_rad -= lat_rad_d
    lon_rad -= lon_rad_d
    return lat_rad, lon_rad

if __name__ == '__main__':
    import sys
    _, name, rad = sys.argv
    rad = float(rad)
    draw_reachable_stops_from_name(name, rad)
