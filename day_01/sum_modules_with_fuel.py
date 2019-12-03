
def calcFuel(mass):
    return max( ( mass // 3 ) - 2, 0 )

def calcTotalFuel(mass):
    fuel_weight = calcFuel( mass )
    if( fuel_weight > 0 ):
        fuel_weight += calcTotalFuel( fuel_weight )
    return fuel_weight;

def main():
    sum_weight = 0;
    with open("input.txt", "r") as f:
        for line in f:
            sum_weight += calcTotalFuel( int( line ) )
    print( "weight+fuel = ", sum_weight )
