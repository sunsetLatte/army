print('"Военкомат"')   
print('Призывник:')   

heigh = 180
age = 25
kids = 0
study = True

if 18 < age < 27:
    if kids < 2:
        if study == False:
            if heigh < 170:
                print('В танкисты')
            elif heigh < 180:
                print('На флот')
            elif heigh < 200:
                print('В десантники')          
        else:
            print('не призывается — на обучении') 
    else:
        print('не призывается — есть дети') 
else:
    print('непризывной возраст')     

