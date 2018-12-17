def pattern(number):
    if number == 1:
        print 1,
        return 1
    else:
        var=pattern(number-1) + 3
        print var,
        return var


pattern(6)