import math
import simplekml

kml = simplekml.Kml()
CIRCLE_VERTS = 40

def draw_circle(name, lat, lon, rad):
    ls = kml.newlinestring(name=name)
    pi_points = [2 * math.pi * x/float(CIRCLE_VERTS)
            for x in xrange(CIRCLE_VERTS + 1)]
    ls.coords = [(rad * math.sin(t) + lon, rad * math.cos(t) + lat)
                for t in pi_points]

def save_kml():
    kml.save('out.kml')
