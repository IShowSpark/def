#def Pindala(külg1:float,külg2:float)->float:
#    """Riistküliku pindala leidmine
#    :param float külg1:Riistküliku(прямоу-ник) esimene(первая) külg(сторона)
#    :param float külg2:Riistküliku(прямоу-ник) teine(вторая) külg(сторона)
#    :rtype:float
#    """


#    s=külg1*külg2
#    return s

#def arithmetic(x:float,y:float,z:str)->float:
#    """deistvija +,-,*,/
#    :param float x: pervoe chislo
#    :param float y: vtoroe chislo
#    :param float z: deistvie
#    :rtype:var
#    """
#    if z=="+":
#        otvet=x+y
#    elif z=="-":
#        otvet=x-y
#    elif z=="*":
#        otvet=x*y
#    elif z=="/":
#        otvet=x/y
#    else:
#        otvet="Неверная операция"
#    return otvet



#def is_year_leap(year:int):
#    if year % 400 == 0:
#        return True
#    if year % 4 == 0 and year % 100 != 0:
#        return True
#    return False

#import math
#def square(a:int):
#    p=4*a
#    s=a**2
#    diagonal=round(a*math.sqrt(2))
#    return p,s,diagonal


#def season(month:int):
#    if month in (12,1,2):
#        return "Зима"
#    elif month in (3,4,5):
#        return "Весна"
#    elif month in (6,7,8):
#        return "Лето"
#    elif month in (9,10,11):
#        return "Осень"

#def bank(a,years):
#    for year in range(years):
#        a*=1.1
#    return a




#def is_prime(number):
#    ans=0
#    if number>0<1000:
#        for i in range(1,number+1):
#            if number%i==0: ans+=1
#        if ans==2:
#            ans=True
#        else:
#            ans=False
#        return ans


#def date(d,m,y):
#    import datetime
#    try:
#        datetime.date(y,m,d)
#    except ValueError:
#        return False
#    else:
#        return True


















