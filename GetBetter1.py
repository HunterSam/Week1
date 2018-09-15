def frameWork(dhaga):
    maxi = len(dhaga[0])
    for i in dhaga:
        if len(i)>maxi:
            maxi = len(i)
    print('* '*maxi)
    for i in dhaga:
        khali = 2*maxi-4-len(i)
        print('* '+i.capitalize()+khali*' '+'*')
    print('* '*maxi)
    return None
#frameWork(['Hello','World','in','a','Frame'])

def sharabi():
    sen1 = 'bottles of beer on the wall,'
    sen2 = 'Take one down and pass it around,'
    for beers in range(99,1,-1):
        if beers == 2:
            print(beers, sen1, beers, sen1[:15] + '.' + '\n' + sen2, beers - 1, sen1[:6]+sen1[7:-1] + '.' + '\n')
            beers -= 1
            break
        print(beers,sen1,beers,sen1[:15]+'.'+'\n'+sen2,beers-1,sen1[:-1]+'.'+'\n')
    print(beers, sen1[:6] + sen1[7:], beers, sen1[:6]+sen1[7:15] + '.' + '\n' + sen2, 'no more bottles of beer on the wall.' + '\n')
    print('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')
    return None
sharabi()

