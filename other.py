def getDivisor(n):
    divisors=[(1,n)]
    i=2
    maxDivisor=n
    while i<maxDivisor:
        if n%i==0:
            divisors.append((i, n//i))
            maxDivisor=n//i
        i+=1
    return divisors

def creatorGrid(numberColumn: int, numberRow: int):
    return [[0*numberRow]*numberColumn]