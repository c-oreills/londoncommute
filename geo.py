def iter_in_rad(stops, x, y, rad):
    max_x, min_x = x + rad, x - rad
    max_y, min_y = y + rad, y - rad
    rad_sq = rad ** 2
    for stop in stops:
        stop_x, stop_y = stop.x, stop.y
        if not ((min_x, min_y) <= (stop_x, stop_y) <= (max_x, max_y)):
            continue
        if (stop_x - x) ** 2 <= rad_sq and (stop_y - y) ** 2 <= rad_sq:
            yield stop
