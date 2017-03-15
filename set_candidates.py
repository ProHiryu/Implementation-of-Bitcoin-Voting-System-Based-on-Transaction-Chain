ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

def set_candidates():
    candidates = []
    candidate_file = open('candidates.txt','r')
    lines = candidate_file.readlines()
    can_num = len(lines)
    for line in lines:
        line = line.strip()
        candidate = line.split(' : ')[0]
        candidates.append(candidate)

    for i in range(int(can_num)):
        print("The {} one:".format(ordinal(i+1)),candidates[i])

    return candidates
