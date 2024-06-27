a = list(map(int,input().split()))
composites = []
primes = []
prime_sum=0
composites_sum=0
for number in a:
    for i in range(2,(number//2)+1):
        if number%i == 0:
            composites.append(number)
            break
    else:
        primes.append(number)
print(f"composites : {composites}\nprimes : {primes}\nsum of primes {sum(primes)}\nsum of composites {sum(composites)}")