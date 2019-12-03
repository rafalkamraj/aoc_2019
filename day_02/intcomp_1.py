import time

def loadProgram( filename ):
    with open( filename, "r" ) as f:
        line = f.readline()
        program = list( map( int, line.split(",") ) )
    return program;

def runProgram( program ):
    result = program.copy();
    instruction_ptr = 0;
    while( 1 ):
        opcode = result[instruction_ptr]
        if( opcode == 99 ):
            #print( "HALT" )
            break;
        srcA = result[instruction_ptr + 1]
        srcB = result[instruction_ptr + 2]
        dst = result[instruction_ptr + 3]
        instruction_ptr += 4;
        if( opcode == 1 ):
            #print( "ADD ", result[srcA], result[srcB] );
            result[dst] = result[srcA] + result[srcB]
        elif( opcode == 2 ) :
            #print( "MUL ", result[srcA], result[srcB] );
            result[dst] = result[srcA] * result[srcB]
        else:
            print( "!OPCODE" );
            break;
    return result;

def testProgram( filename, test_filename ):
    print( "testing ", filename, "..." )
    program = loadProgram( filename )
    result = runProgram( program )
    test = loadProgram( test_filename )

    print( "source: ", program )
    print( "result: ", result )
    print( "test:   ", test )
    if( result == test ):
        print( "Test Passed" )
    else:
        print( "Test Failed" )


def findMagicBrute( magic, program ):
    start_time = time.time();
    iterations = 0
    for i in range( 1, 100 ):
        for j in range( 1, 100 ):
            iterations += 1
            program[1] = i
            program[2] = j
            result = runProgram( program )
            if( result[0] == magic ):
                return [i, j, iterations, time.time() - start_time]
    print( "magic not found! " )
    

def findMagicFast( magic, program ):
    start_time = time.time();
    iterations = 0;
    for i in range( 1, 100 ):
        iterations += 1
        program[1] = i
        program[2] = 99
        result = runProgram( program );
        if( result[0] < magic ):
           continue

        for j in range( 1, 100 ):
            iterations += 1
            program[1] = i
            program[2] = j
            result = runProgram( program )
            if( result[0] > magic ):
                break
            if( result[0] == magic ):
                return [i, j, iterations, time.time() - start_time]
    print( "magic not found!" )

def findMagicFaster( magic, program ):
    start_time = time.time();
    iterations = 0;
    for i in range( 1, 100 ):
        for j in range( 99, 0, -1 ):
            iterations += 1
            program[1] = i
            program[2] = j
            result = runProgram( program )
            if( result[0] < magic ):
                break
            if( result[0] == magic ):
                return [i, j, iterations, time.time() - start_time]
    print( "magic not found!" )
    
def findILessThanMagic( magic, program, iterations_list ):
    start = 1
    end = 99
    while( start < end ):
        i = ( start + end ) // 2
        iterations_list[0] += 1
        program[1] = i
        program[2] = 99
        result = runProgram( program )
        if( result[0] < magic ):
            start = i + 1
        else:
            end = i - 1
    return start

def findJLessThanMagic( magic, program, iterations_list ):
    start = 1
    end = 99
    while( start < end ):
        j = ( start + end ) // 2
        iterations_list[0] += 1
        program[1] = 99
        program[2] = j
        result = runProgram( program )
        if( result[0] < magic ):
            start = j + 1
        else:
            end = j - 1
    return start

def findIGreaterThanMagic( magic, program, start_i, j, iterations_list ):
    start = start_i
    end = 99
    while( start < end ):
        i = ( start + end ) // 2
        iterations_list[0] += 1
        program[1] = i
        program[2] = j
        result = runProgram( program )
        if( result[0] > magic ):
            end = i - 1
        else:
            start = i + 1
    return end

def findJGreaterThanMagic( magic, program, start_j, i, iterations_list ):
    start = start_j
    end = 99
    while( start < end ):
        j = ( start + end ) // 2
        iterations_list[0] += 1
        program[1] = i
        program[2] = j
        result = runProgram( program )
        if( result[0] > magic ):
            end = j - 1
        else:
            start = j + 1
    return end


def findMagicBinary( magic, program ):
    start_time = time.time();
    iterations_list = [ 0 ]
    start_i = findILessThanMagic( magic, program, iterations_list )
    start_j = findJLessThanMagic( magic, program, iterations_list )
    end_i = findIGreaterThanMagic( magic, program, start_i, start_j, iterations_list )
    end_j = findJGreaterThanMagic( magic, program, start_j, start_i, iterations_list )
    
    for i in range( start_i, end_i + 1 ):
        for j in range( end_j, start_j - 1, -1 ):
            iterations_list[0] += 1
            program[1] = i
            program[2] = j
            result = runProgram( program )
            if( result[0] < magic ):
                break
            if( result[0] == magic ):
                return [i, j, iterations_list[0], time.time() - start_time]
    print( "magic not found!" )



def main():
#    testProgram( "test1.txt", "res1.txt" );
#    testProgram( "test2.txt", "res2.txt" );
#    testProgram( "test3.txt", "res3.txt" );

    program = loadProgram( "input.txt" )
    # restore gravity
    program[1] = 12;
    program[2] = 2;
    result = runProgram( program )

    print( "source: ", program )
    print( "result: ", result )

    magic = 19690720
           
    res = findMagicBrute( magic, program )
    print( "brute: magic at i= ", res[0], " j= ", res[1], " iMachine calls= ", res[2], " s= ", res[3] )

    res = findMagicFast( magic, program )
    print( "ifOne: magic at i= ", res[0], " j= ", res[1], " iMachine calls= ", res[2], " s= ", res[3] )

    res = findMagicFaster( magic, program )
    print( "ifTwo: magic at i= ", res[0], " j= ", res[1], " iMachine calls= ", res[2], " s= ", res[3] )

    res = findMagicBinary( magic, program )
    print( "Binry: magic at i= ", res[0], " j= ", res[1], " iMachine calls= ", res[2], " s= ", res[3] )

