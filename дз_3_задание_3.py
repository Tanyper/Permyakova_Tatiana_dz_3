def thesaurus(*names):
    key = {}
    for name in names:
        i = name [0]
        if i in key :
            key[i] += [name]
        else :
            key[i] = [name]
    return key
print (thesaurus("Иван","Мария", "Петр", "Илья","Анастасия", "Аркадий" ))
