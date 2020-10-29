
from math import sqrt, ceil

# Only to time this method
class TimePrime:
    def __init__(self):
        self.__count = 0

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, val):
        self.__count = val

    def prime_list(self):
        # we're going to assume that 2 is a prime - without checking for it
        primes = [2]
        # now get a list of all the numbers greater than 1 and equal the square root of x (rounded up)
        for x in range(2, self.__count+1):
            l = [x for x in range(2, ceil(sqrt(x)))] + primes
            if not all([x%s for s in l]):
                pass
            else:
                primes.append(x)

def time_the_primes():
    import timeit
    timeprime = TimePrime()
    for i in range(1, 11):
        timeprime.count = i*10000
        print("|{counter}|{time}s|".format(counter=timeprime.count, time=round(timeit.timeit(timeprime.prime_list, number=1),3)))

def pretty_print(prime_list):
    prime_dict = {i+1:prime_list[i] for i in range(0,len(prime_list))}
    with open('prime.list.md', 'w') as f:
        for i in prime_dict.keys():
            f.write("|{}|".format(prime_dict[i]))
            if i%50 == 0:
                f.write("\n")

def graph_primes(prime_list):
    prime_dict = {i+1:prime_list[i] for i in range(0,len(prime_list))}
    print(prime_dict[1])
    print(prime_dict[10])
    print(prime_dict[100])
    # print(prime_dict[1000])

def main():
    count = 100000
    # we're going to assume that 2 is a prime - without checking for it
    primes = [2]
    # now get a list of all the numbers greater than 1 and equal the square root of x (rounded up)
    for x in range(2, count+1):
        l = [x for x in range(2, ceil(sqrt(x)))] + primes
        if not all([x%s for s in l]):
            pass
        else:
            primes.append(x)
    # print(primes)
    # graph_primes(primes)
    pretty_print(primes)


if __name__ == "__main__":
    main()
    # time_the_primes()

