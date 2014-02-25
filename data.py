from collections import defaultdict, namedtuple
from csv import DictReader

from geo import iter_in_rad


class fields(object):
    stop_id = 'Stop_Code_LBSL'
    name = 'Stop_Name'
    x = 'Location_Easting'
    y = 'Location_Northing'
    route_id = 'Route'

Stop = namedtuple('Stop', 'id name x y')
Route = namedtuple('Route', 'route_id stop_id')

def parse_stops():
    stop_csv = DictReader(open('stops.csv', 'r'))
    stops = []
    for stop in stop_csv:
        if not (stop[fields.x] and stop[fields.y]):
            continue
        id = stop[fields.stop_id]
        name = stop[fields.name]
        x = int(stop[fields.x])
        y = int(stop[fields.y])
        stop = Stop(id, name, x, y)
        stops.append(stop)
    return stops

def index_stops(stops):
    stops_by_id = {}
    stops_by_name = {}
    for stop in stops:
        stops_by_id[stop.id] = stop
        stops_by_name[stop.name] = stop
    return stops_by_id, stops_by_name

def get_nearby_stops(stops, x, y, rad):
    return list(iter_in_rad(stops, x, y, rad))

def parse_routes():
    routes_csv = DictReader(open('routes.csv', 'r'))
    routes = []
    for route in routes_csv:
        route_id = route[fields.route_id]
        stop_id = route[fields.stop_id]
        route = Route(route_id, stop_id)
        routes.append(route)
    return routes

def index_routes(routes, stops_by_id):
    routes_by_stop_id = defaultdict(set)
    stops_by_route_id = defaultdict(set)
    for route in routes:
        routes_by_stop_id[route.stop_id].add(route)
        stop = stops_by_id.get(route.stop_id)
        if stop:
            stops_by_route_id[route.route_id].add(stop)
    return routes_by_stop_id, stops_by_route_id

stops = parse_stops()
stops_by_id, stops_by_name = index_stops(stops)
routes = parse_routes()
routes_by_stop_id, stops_by_route_id = index_routes(routes, stops_by_id)

def get_reachable_stops(x, y, rad):
    near_work_stops = get_nearby_stops(stops, x, y, 700)
    near_work_route_ids = {r.route_id
            for stop in near_work_stops
            for r in routes_by_stop_id[stop.id]}

    reachable_stops = {s
            for route_id in near_work_route_ids
            for s in stops_by_route_id[route_id]}
    return reachable_stops

def get_reachable_stops_from_name(name, rad):
    stop = stops_by_name[name]
    return get_reachable_stops(stop.x, stop.y, rad)

