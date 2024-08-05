def gcd(A, B):
    if A % B == 0:
        return B
    elif B % A == 0:
        return A
    else:
        if A > B:
            smaller, larger = B, A
        else:
            smaller, larger = A, B

        i = smaller

        while i > 1:
            if smaller % i == 0 and larger % i == 0:
                return i
            else:
                i -= 1


def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


if __name__ == "__main__":
    print(gcd(3, 6))
    print(gcd(4, 6))
    print(gcd(132, 10))
