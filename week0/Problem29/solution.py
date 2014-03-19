def gcd (a,b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, a)
    else:
        return gcd(a, b-a)

def simplify_fraction(fraction):
    if fraction[1] == 0:
        return False
    n = gcd(fraction[0],fraction[1])
    x = fraction[0] / n
    y = fraction[1] / n
    return (int(x),int(y))
