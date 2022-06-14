# 최대공약수 greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수 least commin mutiplier
def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    answer = 0
    lcm_a = a[0]
    gcd_b = b[0]

    for i in range(1, len(a)):
        lcm_a = lcm(lcm_a, a[i])
    
    for i in range(1, len(b)):
        gcd_b = gcd(gcd_b, b[i])

    print(lcm_a, gcd_b)
    
    for i in range(lcm_a, gcd_b+1):
        if i % lcm_a == 0 and gcd_b % i == 0:
            answer += 1
    
    return answer

getTotalX([3, 4], [24, 48])