

def testPassword( password ):
    if( len( password ) != 6 ):
        return False

    twin_neighbours = 0
    for x in range( 0, 5 ):
        if( password[x] > password[x+1] ):
            return False
        if( password[x] == password[x+1] ):
            twin_neighbours += 1

    if( twin_neighbours == 0 ):
        return False
    
    return True

def testPassword2( password ):
    if( not testPassword( password ) ):
        return False

    has_2_chars_group = False

    groups = []
    num_chars = 0
    character = "0"

    twin_neighbours = 0
    for x in range( 0, 5 ):
        if( password[x] == password[x+1] ):
            if( num_chars == 0 ):
                num_chars = 2
                character = password[x]
            else:
                num_chars += 1
        else:
            if( num_chars > 0 ):
                if( num_chars == 2 ):
                    has_2_chars_group = True
                groups.append( num_chars )
                num_chars = 0
                
    if( num_chars > 0 ):
        if( num_chars == 2 ):
            has_2_chars_group = True
        groups.append( num_chars )
        num_chars = 0
      
    return has_2_chars_group


def main():
    total_correct_passwords = 0
    total_cp2 = 0
    for x in range( 235741, 706949 ):
#    for x in range( 111122, 111124 ):
        password = str( x )
        if( testPassword( password ) ):
            total_correct_passwords += 1
        if( testPassword2( password ) ):
             total_cp2 += 1

    print( "test 1 found ", total_correct_passwords )
    print( "test 2 found ", total_cp2 )
