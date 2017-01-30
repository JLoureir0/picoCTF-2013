#!/usr/bin/env python2

p =  9648423029010515676590551740010426534945737639235739800643989352039852507298491399561035009163427050370107570733633350911691280297777160200625281665378483
q =  11874843837980297032092405848653656852760910154543380907650040190704283358909208578251063047732443992230647903887510065547947313543299303261986053486569407
e =  65537
c =  83208298995174604174773590298203639360540024871256126892889661345742403314929861939100492666605647316646576486526217457006376842280869728581726746401583705899941768214138742259689334840735633553053887641847651173776251820293087212885670180367406807406765923638973161375817392737747832762751690104423869019034

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# x = mulinv(b) mod n, (x * b) % n == 1
def modular_multiplicative_inverse(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
# =================================================================

t = (p-1)*(q-1)
d = modular_multiplicative_inverse(e,t)
n = p*q

decrypted_message = pow(c,d,n)

print decrypted_message
