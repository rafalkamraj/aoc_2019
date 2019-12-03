def calcFule(mass):
    return max( ( mass // 3 ) - 2, 0 )

def main():
    sum_weight = 0;
    with open("input.txt", "r") as f:
        for line in f:
            sum_weight += calcFule( int( line ) )
    f.close()
    print( "sum weight = ", sum_weight )
