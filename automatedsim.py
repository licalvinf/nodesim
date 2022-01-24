import mainsim


def prompt():
    reqlb = int(input("Lower bound of required nodes: "))
    requb = int(input("Upper bound of required nodes: "))
    totlb = int(input("Lower bound of total nodes: "))
    totup = int(input("Upper bound of total nodes: "))
    reqrange = range(reqlb, requb+1)
    totrange = range(totlb, totup+1)
    iterations = int(input("Number of iterations: "))
    return reqrange, totrange, iterations


def rangeiterator(reqrange, totrange, iterations):
    reqlist = []
    for reqs in reqrange:
        totlist = []
        isodd = False
        if (reqs - 2) % 3 == 0:
            continue
        if reqs * 2 % 3 != 0:
            isodd = True
        for tots in totrange:
            if reqs > tots:
                continue
            avg = mainsim.sim(iterations, tots, reqs, isodd)
            totlist.append(avg)
        reqlist.append(totlist)
    return reqlist


def main():
    reqrange, totrange, iterations = prompt()
    avglist = rangeiterator(reqrange, totrange,iterations)
    print(avglist)


if __name__ == "__main__":
    main()

