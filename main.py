# This is a representation for the rubik's cube

# {'top': [x,x,x,x,x,x,x,x], 'bottom': [x,x,x,x,x,x,x,x], 'front': [x,x,x,x,x,x,x,x], 'back': [x,x,x,x,x,x,x,x], 'left': [x,x,x,x,x,x,x,x], 'right': [x,x,x,x,x,x,x,x]}
# X is a representation for a color, it can be a number, a char, or whatever makes you happy

# The solution is, for example:

# {'top': [0,0,0,0,0,0,0,0], 'bottom': [1,1,1,1,1,1,1,1], 'front': [2,2,2,2,2,2,2,2], 'back': [3,3,3,3,3,3,3], 'left': [4,4,4,4,4,4,4,4], 'right': [5,5,5,5,5,5,5,5]}


def print_cube(cube):
    print('#####################')
    print('Top: ', cube['top'])
    print('Front: ', cube['front'])
    print('Left: ', cube['left'])
    print('Right: ', cube['right'])
    print('Back: ', cube['back'])
    print('Bottom: ', cube['bottom'])
    print('#####################')


# Cube is a cube representation like the one above
# Face can be one of the following: 'top', 'bottom', 'front', 'back', 'right', 'left'
# Orientation can be CW (clockwise) and CCW (counter clockwise)
def move(cube, face, orientation):
    cube = move_face(cube, face, orientation)
    if (face == 'top'):
        cube = move_top_collaterals(cube, orientation)
        if (orientation == 'cw'):
            print('Top CW')
        elif (orientation == 'ccw'):
            print('Top CCW')
    elif (face == 'bottom'):
        cube = move_bottom_collaterals(cube, orientation)
        if (orientation == 'cw'):
            print('Bottom CW')
        elif (orientation == 'ccw'):
            print('Bottom CCW')
    elif (face == 'front'):
        cube = move_front_collaterals(cube, orientation)
        if (orientation == 'cw'):
            print('Front CW')
        elif (orientation == 'ccw'):
            print('Front CCW')
    elif (face == 'back'):
        cube = move_back_collaterals(cube, orientation)
        if (orientation == 'cw'):
            print('Back CW')
        elif (orientation == 'ccw'):
            print('Back CCW')
    elif (face == 'left'):
        cube = move_left_collaterals(cube, orientation)
        if (orientation == 'cw'):
            print('Left CW')
        elif (orientation == 'ccw'):
            print('Left CCW')
    elif (face == 'right'):
        cube = move_right_collaterals(cube, orientation)
        if (orientation == 'cw'):
            print('Right CW')
        elif (orientation == 'ccw'):
            print('Right CCW')
    return cube


def move_face(cube, face, orientation):
    if (orientation == 'cw'):
        temp = cube[face][0]
        cube[face][0] = cube[face][5]
        cube[face][5] = cube[face][7]
        cube[face][7] = cube[face][2]
        cube[face][2] = temp
        temp = cube[face][1]
        cube[face][1] = cube[face][3]
        cube[face][3] = cube[face][6]
        cube[face][6] = cube[face][4]
        cube[face][4] = temp
    elif (orientation == 'ccw'):
        temp = cube[face][0]
        cube[face][0] = cube[face][2]
        cube[face][2] = cube[face][7]
        cube[face][7] = cube[face][5]
        cube[face][5] = temp
        temp = cube[face][1]
        cube[face][1] = cube[face][4]
        cube[face][4] = cube[face][6]
        cube[face][6] = cube[face][3]
        cube[face][3] = temp        
    return cube


def move_top_collaterals(cube, orientation):
    if (orientation == 'cw'):
        temp = cube['back'][2]
        cube['back'][2] = cube['left'][2]
        cube['left'][2] = cube['front'][2]
        cube['front'][2] = cube['right'][2]
        cube['right'][2] = temp
        temp = cube['back'][0]
        cube['back'][0] = cube['left'][0]
        cube['left'][0] = cube['front'][0]
        cube['front'][0] = cube['right'][0]
        cube['right'][0] = temp
        temp = cube['back'][1]
        cube['back'][1] = cube['left'][1]
        cube['left'][1] = cube['front'][1]
        cube['front'][1] = cube['right'][1]
        cube['right'][1] = temp
    elif (orientation == 'ccw'):
        temp = cube['back'][2]
        cube['back'][2] = cube['right'][2]
        cube['right'][2] = cube['front'][2]
        cube['front'][2] = cube['left'][2]
        cube['left'][2] = temp
        temp = cube['back'][0]
        cube['back'][0] = cube['right'][0]
        cube['right'][0] = cube['front'][0]
        cube['front'][0] = cube['left'][0]
        cube['left'][0] = temp
        temp = cube['back'][1]
        cube['back'][1] = cube['right'][1]
        cube['right'][1] = cube['front'][1]
        cube['front'][1] = cube['left'][1]
        cube['left'][1] = temp
    return cube


def move_bottom_collaterals(cube, orientation):
    if (orientation == 'cw'):
        temp = cube['back'][5]
        cube['back'][5] = cube['right'][5]
        cube['right'][5] = cube['front'][5]
        cube['front'][5] = cube['left'][5]
        cube['left'][5] = temp
        temp = cube['back'][6]
        cube['back'][6] = cube['right'][6]
        cube['right'][6] = cube['front'][6]
        cube['front'][6] = cube['left'][6]
        cube['left'][6] = temp
        temp = cube['back'][7]
        cube['back'][7] = cube['right'][7]
        cube['right'][7] = cube['front'][7]
        cube['front'][7] = cube['left'][7]
        cube['left'][7] = temp
    elif (orientation == 'ccw'):
        temp = cube['back'][5]
        cube['back'][5] = cube['left'][5]
        cube['left'][5] = cube['front'][5]
        cube['front'][5] = cube['right'][5]
        cube['right'][5] = temp
        temp = cube['back'][6]
        cube['back'][6] = cube['left'][6]
        cube['left'][6] = cube['front'][6]
        cube['front'][6] = cube['right'][6]
        cube['right'][6] = temp
        temp = cube['back'][7]
        cube['back'][7] = cube['left'][7]
        cube['left'][7] = cube['front'][7]
        cube['front'][7] = cube['right'][7]
        cube['right'][7] = temp
    return cube


def move_front_collaterals(cube, orientation):
    if (orientation == 'cw'):
        temp = cube['top'][5]
        cube['top'][5] = cube['left'][7]
        cube['left'][7] = cube['bottom'][5]
        cube['bottom'][5] = cube['right'][0]
        cube['right'][0] = temp
        temp = cube['top'][6]
        cube['top'][6] = cube['left'][4]
        cube['left'][4] = cube['bottom'][6]
        cube['bottom'][6] = cube['right'][4]
        cube['right'][4] = temp
        temp = cube['top'][7]
        cube['top'][7] = cube['left'][2]
        cube['left'][2] = cube['bottom'][7]
        cube['bottom'][7] = cube['right'][5]
        cube['right'][5] = temp
    elif (orientation == 'ccw'):
        temp = cube['top'][5]
        cube['top'][5] = cube['right'][0]
        cube['right'][0] = cube['bottom'][5]
        cube['bottom'][5] = cube['left'][7]
        cube['left'][7] = temp
        temp = cube['top'][6]
        cube['top'][6] = cube['right'][4]
        cube['right'][4] = cube['bottom'][6]
        cube['bottom'][6] = cube['left'][4]
        cube['left'][4] = temp
        temp = cube['top'][7]
        cube['top'][7] = cube['right'][5]
        cube['right'][5] = cube['bottom'][7]
        cube['bottom'][7] = cube['left'][2]
        cube['left'][2] = temp
    return cube


def move_back_collaterals(cube, orientation):
    if (orientation == 'cw'):
        temp = cube['top'][0]
        cube['top'][0] = cube['right'][2]
        cube['right'][2] = cube['bottom'][0]
        cube['bottom'][0] = cube['left'][5]
        cube['left'][5] = temp
        temp = cube['top'][1]
        cube['top'][1] = cube['right'][4]
        cube['right'][4] = cube['bottom'][1]
        cube['bottom'][1] = cube['left'][3]
        cube['left'][3] = temp
        temp = cube['top'][2]
        cube['top'][2] = cube['right'][7]
        cube['right'][7] = cube['bottom'][2]
        cube['bottom'][2] = cube['left'][0]
        cube['left'][0] = temp
    elif (orientation == 'ccw'):
        temp = cube['top'][0]
        cube['top'][0] = cube['left'][5]
        cube['left'][5] = cube['bottom'][0]
        cube['bottom'][0] = cube['right'][2]
        cube['right'][2] = temp
        temp = cube['top'][1]
        cube['top'][1] = cube['left'][3]
        cube['left'][3] = cube['bottom'][1]
        cube['bottom'][1] = cube['right'][4]
        cube['right'][4] = temp
        temp = cube['top'][2]
        cube['top'][2] = cube['left'][0]
        cube['left'][0] = cube['bottom'][2]
        cube['bottom'][2] = cube['right'][7]
        cube['right'][7] = temp
    return cube


def move_right_collaterals(cube, orientation):
    if (orientation == 'cw'):
        temp = cube['top'][7]
        cube['top'][7] = cube['front'][7]
        cube['front'][7] = cube['bottom'][0]
        cube['bottom'][0] = cube['back'][0]
        cube['back'][0] = temp
        temp = cube['top'][4]
        cube['top'][4] = cube['front'][4]
        cube['front'][4] = cube['bottom'][3]
        cube['bottom'][3] = cube['back'][3]
        cube['back'][3] = temp
        temp = cube['top'][2]
        cube['top'][2] = cube['front'][2]
        cube['front'][2] = cube['bottom'][5]
        cube['bottom'][5] = cube['back'][5]
        cube['back'][5] = temp
    elif (orientation == 'ccw'):
        temp = cube['top'][7]
        cube['top'][7] = cube['back'][0]
        cube['back'][0] = cube['bottom'][0]
        cube['bottom'][0] = cube['front'][7]
        cube['front'][7] = temp
        temp = cube['top'][4]
        cube['top'][4] = cube['back'][3]
        cube['back'][3] = cube['bottom'][3]
        cube['bottom'][3] = cube['front'][4]
        cube['front'][4] = temp
        temp = cube['top'][2]
        cube['top'][2] = cube['back'][5]
        cube['back'][5] = cube['bottom'][5]
        cube['bottom'][5] = cube['front'][2]
        cube['front'][2] = temp
    return cube


def move_left_collaterals(cube, orientation):
    if (orientation == 'cw'):
        temp = cube['top'][0]
        cube['top'][0] = cube['back'][7]
        cube['back'][7] = cube['bottom'][7]
        cube['bottom'][7] = cube['front'][0]
        cube['front'][0] = temp
        temp = cube['top'][3]
        cube['top'][3] = cube['back'][4]
        cube['back'][4] = cube['bottom'][4]
        cube['bottom'][4] = cube['front'][3]
        cube['front'][3] = temp
        temp = cube['top'][5]
        cube['top'][5] = cube['back'][2]
        cube['back'][2] = cube['bottom'][2]
        cube['bottom'][2] = cube['front'][5]
        cube['front'][5] = temp
    elif (orientation == 'ccw'):
        temp = cube['top'][0]
        cube['top'][0] = cube['front'][0]
        cube['front'][0] = cube['bottom'][7]
        cube['bottom'][7] = cube['back'][7]
        cube['back'][7] = temp
        temp = cube['top'][3]
        cube['top'][3] = cube['front'][3]
        cube['front'][3] = cube['bottom'][4]
        cube['bottom'][4] = cube['back'][4]
        cube['back'][4] = temp
        temp = cube['top'][5]
        cube['top'][5] = cube['front'][5]
        cube['front'][5] = cube['bottom'][2]
        cube['bottom'][2] = cube['back'][2]
        cube['back'][2] = temp
    return cube


# This is a possible scenario with top being 'b', front being 'o', right being 'y', left being 'r', back being 'g' and bottom being 'w' ->

my_cube = {
    'top': ['w', 'y', 'y', 'o', 'g', 'b', 'r', 'w'],
    'bottom': ['g', 'g', 'w', 'o', 'y', 'r', 'g', 'b'],
    'front': ['o', 'w', 'y', 'o', 'o', 'o', 'y', 'g'],
    'back': ['g', 'w', 'r', 'g', 'r', 'b', 'b', 'r'],
    'left': ['g', 'w', 'r', 'b', 'y', 'o', 'b', 'y'],
    'right': ['o', 'w', 'w', 'r', 'r', 'b', 'b', 'y']
}

# Testing
print_cube(my_cube)
move(my_cube, 'top', 'cw')
print_cube(my_cube)
