ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

def set_candidates():
    candidates = []
    can_num = input('How many candidates:')
    for i in range(int(can_num)):
        candidate = input("The {} one:".format(ordinal(i+1)))
        candidates.append(candidate)

    return candidates
