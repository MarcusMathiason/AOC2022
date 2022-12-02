#   Part 1
with open('input.txt') as f:
    most = 0; 
    tmp = 0
    for i in f.read().splitlines():
        if i != '':
            tmp = tmp + int(i)
        else:
            if tmp > most:
                most = tmp
            tmp = 0
    print(f'Most: {most}')

#   Part 2
with open('input.txt') as f:
    topThree = [0, 0, 0]
    tmp = 0
    for i in f.read().splitlines():
        if i!= '':
            tmp = tmp + int(i)
        else:
            if tmp > topThree[0]:
                topThree[0] = tmp
                topThree.sort()
            tmp = 0
    print(f'Top three: {topThree}')
    print(f'Top three total: {sum(topThree)}')