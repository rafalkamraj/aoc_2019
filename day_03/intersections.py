def genKey( x, y ):
    return str( x ) + "_" + str( y )

def addWire( start, steps_x, steps_y, mask, board, mask_to_find, cross_points, start_length, lengths ):
    x = start[0]
    y = start[1]
    current_length = start_length
    while( steps_x != 0 or steps_y != 0 ):
        if( steps_x > 0 ):
            x += 1
            steps_x -= 1
        elif( steps_x < 0 ):
            x -= 1
            steps_x += 1
        elif( steps_y > 0 ):
            y += 1
            steps_y -= 1
        else:
            y -= 1
            steps_y += 1

        key = genKey( x, y )

        current_length += 1
        if( not key in lengths ):
            lengths[key] = current_length

        if( mask_to_find != 0 and ( key in board ) ):
            cell = board[key]
            cell |= mask
            board[key] = cell;
            if( cell & mask_to_find == mask_to_find ):
                cross_points[key] = (x, y)
        else:
            board[key] = mask

def addCircuit( start, circ, mask, board, mask_to_find, cross_points, lengths ):
    x = start[0]
    y = start[1]
    current_length = 0;
    for move in circ:
        move_type = move[0]
        move_length = int( move[1:] );
        if( move_type == "R" ):
            addWire( (x, y), move_length, 0, mask, board, mask_to_find, cross_points, current_length, lengths )
            x += move_length
        elif( move_type == "L" ):
            addWire( (x, y), -move_length, 0, mask, board, mask_to_find, cross_points, current_length, lengths )
            x -= move_length
        elif( move_type == "U" ):
            addWire( (x, y), 0, move_length, mask, board, mask_to_find, cross_points, current_length, lengths )
            y += move_length
        elif( move_type == "D" ):
            addWire( (x, y), 0, -move_length, mask, board, mask_to_find, cross_points, current_length, lengths )
            y -= move_length

        current_length += move_length

def findClosestCross( start, cross_points ):
    closest_dist = 1000000
    closest_point = [0,0]
    for p in cross_points.values():
        dist = abs( p[0] - start[0] ) + abs( p[1] - start[1] )
        if( dist < closest_dist ):
            closest_dist = dist
            closest_point[0] = p[0]
            closest_point[1] = p[1]

    print( "dist = ", closest_dist, " at p = ", closest_point, " d = ", ( abs( closest_point[0] - start[0] ) + abs( closest_point[1] - start[1] ) ) )
    return closest_point

def findCrossWithSmallestLength( cross_points, wire_one_lengths, wire_two_lengths ):
    closest_distance = 1000000
    closest_cross = [0, 0]
    for p in cross_points.values():
        key = genKey( p[0], p[1] )
        print( "testing cross at= ", p, " d1 = ", wire_one_lengths[key], " w2 = ", wire_two_lengths[key] )
        distance = wire_one_lengths[key] + wire_two_lengths[key]
        if( closest_distance > distance ):
            closest_distance = distance
            closest_cross[0] = p[0]
            closest_cross[1] = p[1]

    print( "dist = ", closest_distance, " closest_cross = ", closest_cross )
    return closest_cross

def main():
    with open("input.txt", "r") as f:
#    with open("test.txt", "r") as f:
        wire_one = list( map( str, f.readline().split(",") ) )
        wire_two = list( map( str, f.readline().split(",") ) )
    start = (1, 1)
    bread_board = {}
    cross_points = {}
    wire_one_lengths = {}
    wire_two_lengths = {}
    addCircuit( start, wire_one, 1, bread_board, 0, cross_points, wire_one_lengths )
    addCircuit( start, wire_two, 2, bread_board, 3, cross_points, wire_two_lengths )
    #find closest cross to central port (1,1)
    print( "closest cross to start is ", findClosestCross( start, cross_points ) )
    print( "smallest length cross is ", findCrossWithSmallestLength( cross_points, wire_one_lengths, wire_two_lengths ) )

    print( cross_points )
    
