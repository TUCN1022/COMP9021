# Written by Yanglin CHEN for COMP9021
#
# Let k >= 3 be given. The Somos-k sequence is the sequence
# (s_1, s_2, s_3, ...) that is defined as follows.
# * The first k terms of the sequence (i.e., s_1, s_2, ..., s_k)
#   are all equal to 1.
# * Then any term of the sequence (i.e., s_n with n > k) is
#   a fraction whose denominator is the term k positions before
#   (i.e., s_{n-k}) and whose numerator is the sum of
#   - the product of the term before and the term
#     k-1 positions before (i.e., s_{n-1} x s_{n-k+1}),
#   - the product of the term 2 positions before and the term
#     k-2 positions before (i.e., s_{n-2} x s_{n-k+2}),
#   - ...
#   - if k is even, the square of the term that sits in the middle
#     of the sequence consisting of the k-1 terms before.
#
#  Illustration for k = 6:
#  * * * * *
#      |       Raise this guy to the power 2
#    |___|     Multiply these two guys
#  |_______|   Multiply these two guys
#              Add up the three products to get the numerator
#
#  Illustration for k = 7:
#  * * * * * *
#      |_|       Multiply these two guys
#    |_____|     Multiply these two guys
#  |_________|   Multiply these two guys
#                Add up the three products to get the numerator
#
# See https://www.youtube.com/watch?v=p-HN_ICaCyM&t=616s



from fractions import Fraction


# Returns the list consisting of the n first terms
# of the Somos-k sequence, as strings,
# for k >= 3 and n >= 1.
def somos_sequence(k, n):
    return [str(fraction) for fraction in somos(k, n)]

# Returns the list consisting of the n first terms
# of the Somos-k sequence, as fractions,
# for k >= 3 and n >= 1.
def somos(k, n):
    if n <= k:
        return [Fraction(1)] * n
    L = [Fraction(1)] * k
    # mid_point = (k-1)//2
    for i in range(k,n):
        L = L+[Fraction(next_somos(k,L))]
    return L
        
# Returns the list consisting of the p first terms
# of the Somos-k sequence that are integers,
# as integers, with p as large and possible and
# bounded by n, for k >= 3 and n >= 1.

def integer_somos_sequence(k, n):
    if n <= k:
        return [1] * n
    L = [Fraction(1)] * k
    for i in range(k,n):
        fraction = next_somos(k, L)
        if int(fraction) == fraction:
            L = L + [Fraction(fraction)]
        else:
            break
    return [fraction.numerator for fraction in L]

def next_somos(k, L):
    mid_point =(k-1) // 2 + 1
    r = 0
    for j in range(1, mid_point):
        r += L[len(L)-j]*L[len(L)-k+j]
    if k % 2 == 0:
        r += L[len(L)-mid_point] ** 2
    return r/L[len(L)-k]


print( integer_somos_sequence(6, 50))