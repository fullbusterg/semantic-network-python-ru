def answer(quest):
    f = open ('data.txt')
    dataset = []

    for line in f:
        word = line.split()
        dataset.append(word)
    f.close()

    for s in dataset:
        if s[0] in quest and s[1] in quest:
            return s[2]

        if s[2] in quest:
            if 'ли' in quest:
                for s1 in dataset:
                    if s[0] == s1[0] and  s1[1] in quest and s1[2] in quest:
                        return 'Да'
            else:
                for s1 in dataset:
                    if s[0] == s1[0] and  s1[1] in quest and s1[2] in quest:
                        for s2 in dataset:
                            if s1[0] == s2[0] and s2[1] in quest and s2[2] not in quest:
                                return s2[2]

        if s[0] in quest and s[1] not in quest and s[2] not in quest:
            for s1 in dataset:
                if s1[1] in quest:
                    if s1[0] == s[2]:
                        return s1[2]
    print(quest)
    return 'Нет'


def question_format(quest):
    strip = []
    file = open("format.txt")
    format = []

    for line in file:
        format.append(line.split())

    for word in question:
        word = word.lower().strip('?').strip(',')
        if 'у' in strip:
            word = word.rstrip('а')
        for line in format:
            if word.lower() == line[0]:
                if '_' in line[2]:
                    s = line[2].replace('_',' ').split()
                    strip.append(s[0])
                    strip.append(s[1])
                    continue
                else:
                    word = line[2]
        strip.append(word)

    file.close()
    return strip


while(True):
    question = input().split()
    quest = question_format(question)
    print(quest)
    print(answer(quest))
