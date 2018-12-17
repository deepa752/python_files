def pattern(number):
    if number == 1:
        print 1,
        return 1
    elif number % 2 == 0:
        var = pattern(number - 1) + 3
        print var,
        return var 
    else:
        var= pattern(number - 1) * 2
        print var,
        return var
pattern(6)        