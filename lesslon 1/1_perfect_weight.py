def get_perfect_weight ():

    print ('Введите ваше имя')
    name = input()
    
    print ('Введите ваш рост')
    heigth = input()

    perfect_weight = (int(heigth)-110)*1.15
    if perfect_weight < 0:
        print (name + ', ваш вес уже оптимальный')
    else:
        print (name + ', ваш идеальный вес составляет ' + str(int(perfect_weight)) + ' кг')

get_perfect_weight()