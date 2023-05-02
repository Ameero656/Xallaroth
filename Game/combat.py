from player import Player

level0= [ 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 'p', 0, 0, 0, 0, 'e', 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

key = {'player' : 'p', 'none' : 0, 'void' : -1, 'obstacle' : 1, 'e' : 'enemy'}
rev_key = {'p': 'player', 0: 'none', -1: 'void', 1: 'obstacle', 'enemy': 'e'}




def validate_movement(move_pos, controller_pos, movement, level):

    px, py = controller_pos
    x, y = move_pos

    distance = abs(py-y) + abs(px-x)
    print('d=', distance)
    if distance > movement:
        print('Insufficient movement for specified location')
        return False
    if level[x][y] != key['none']:
        print('Obstacle in the way')
        return False
    print('Sufficient distance for specified location')
    return True
def get_id_pos(level, id):
    global key

    x, y = 0, 0

    for y, col in enumerate(level):
        for x, point in enumerate(col):
            if point == id:
                print(f'Get_controller_pos is returning {x, y}')
                return (x, y)

def move(pos, movement, level, id): # {pos} is tuple
    global key

    x, y = pos
    controller_pos = get_id_pos(level, id) # returns tuple: (x, y)
    if validate_movement(pos, controller_pos, movement, level):
        level[y][x] = id
        level[controller_pos[1]][controller_pos[0]] = key['none']


def display_level(level):

    for row in level:
        for point in row:
            print('|', end = '')
            print(point, end = '')
        print('|')

def main(level, *args):
    
    levels = {'0' : level0}
    level = levels[level]

    display_level(level)
    id = input("id:")
    x = int(input('x:'))
    y = int(input('y:'))
    movement = int(input('Movement Capability:'))
    move((x, y), movement, level, id)


