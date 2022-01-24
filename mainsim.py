from math import floor
from queue import Queue
import random
import numpy


def prompt():
    req = int(input("Enter how many boosted skills this class uses:"))
    while req < 3 or (req - 2) % 3 == 0:
        req = int(input("Error: Unsupported/non-optimal boosts: Enter how many boosted skills this class uses:"))
    tot = int(input("Enter the total number of boostable skills:"))
    iterations = int(input("Enter number of tests to run: "))
    isodd = False
    if req * 2 % 3 != 0:
        isodd = True
    return tot, req, iterations, isodd


def generatenode(tot):
    newnode = random.sample(range(tot), 3)
    newnode[0] += 0.5
    return newnode


def validnode(nodearray, isodd, req):
    for j in nodearray:
        if isodd and j > req + 1:
            return "INVALID"
        if not isodd and j > req:
            return "INVALID"
    return "VALID"


def fullness(nodearray, req, isodd):
    count = 0
    full = True
    for g in nodearray:
        if count < req:
            if g > 2.5:
                full = False
                return "OVERFLOW"
            if g < 2:
                full = False
        if count == req and isodd:
            if g > 1.5:
                full = False
                return "OVERFLOW"
            if g < 1:
                full = False
        if count == req and not isodd:
            if g > 0:
                return "OVERFLOW"
        if count > req:
            if g > 0:
                return "OVERFLOW"
        count += 1
    if full:
        return "FINISH"
    else:
        return "NOT FULL"


def sim(iterations, tot, req, isodd):
    iters = 0
    itersum = 0
    while iters < iterations:
        nodeCount = 0
        checkPassed = False
        q1 = Queue()
        q2 = Queue()
        q1.put(numpy.zeros(tot))
        while nodeCount < 10000 and checkPassed is False:
            curr = generatenode(tot)
            nodeCount += 1
            if validnode(curr, isodd, req) == "INVALID":
                # print("invalid")
                continue
            if not q1.empty():
                while not q1.empty():
                    node_list = q1.get()
                    q2.put(node_list)
                    appended_list = node_list.copy()
                    # print(appended_list)
                    for x in curr:
                        xf = floor(x)
                        if x % 1 != 0 and appended_list[xf] % 1 != 0:
                            continue
                        elif x % 1 != 0:
                            appended_list[xf] += 1.5
                        else:
                            appended_list[xf] += 1

                    nodestate = fullness(appended_list, req, isodd)
                    if nodestate == "FINISH":
                        checkPassed = True
                        break
                    if nodestate == "NOT FULL":
                        q2.put(appended_list)
            else:
                while not q2.empty():
                    node_list = q2.get()
                    q1.put(node_list)
                    appended_list = node_list.copy()
                    # print(appended_list)
                    for x in curr:
                        xf = floor(x)
                        if x % 1 != 0 and appended_list[xf] % 1 != 0:
                            continue
                        elif x % 1 != 0:
                            appended_list[xf] += 1.5
                        else:
                            appended_list[xf] += 1
                    nodestate = fullness(appended_list, req, isodd)
                    if nodestate == "FINISH":
                        checkPassed = True
                        break
                    if nodestate == "NOT FULL":
                        q1.put(appended_list)
        iters += 1
        itersum += nodeCount
    avg_nodes = itersum / iterations
    return avg_nodes


def main():
    tot, req, iterations, isodd = prompt()
    avg = sim(iterations, tot, req, isodd)
    print(avg)


if __name__ == "__main__":
    main()
