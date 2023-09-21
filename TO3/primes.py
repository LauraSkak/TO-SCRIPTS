candidates=list(range(2,30+1))
primes=[]

for number in candidates:
    is_prime=True
    for prime in primes:
        if number/prime%1==0:
            is_prime=False
    if is_prime:
        primes.append(number)
print(primes)