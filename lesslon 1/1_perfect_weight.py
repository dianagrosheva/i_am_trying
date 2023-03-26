def get_perfect_weight (name, height):
    perfect_weight = (height-110)*1.15
    if perfect_weight < 0:
        print (name + ', ваш вес уже оптимальный')
    else:
        print (int(perfect_weight))

get_perfect_weight('Диана', 95)
