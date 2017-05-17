def set_voters():
    voters = []
    voter_file = open('voters.txt', 'r')
    lines = voter_file.readlines()
    for line in lines:
        line = line.strip()
        voters.append(line)

    return voters
