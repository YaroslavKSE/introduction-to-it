def shift(offset, points):
    for point in points:
        type_of_points = type(point)
        if type_of_points == dict:
            point['x'] += offset['x']
            point['y'] += offset['y']
        elif type_of_points == str:
            point.split()
            int((point[7] + point[8])) + offset['x']
            int((point[16] + point[17])) + offset['y']
    return points


polyline = [ { 'x': 0, 'y': 0 },
             { 'x': 10, 'y': 10 },
            '{ "x": 20, "y": 20 }',
             { 'x': 30, 'y': 30 } ]

user_input = input('Enter coordinates to move:').split()
path = (shift({ 'x': int(user_input[0]), 'y': int(user_input[1]) }, polyline))
print(f'path: \n{path}')
