def make_readable(seconds):
    if seconds > 359999:
        return "error! the input "+ str(seconds) +" exced the limit of 359999"
    hh = 0
    mm = 0
    ss = 0
    time = ""
    for x in range(seconds):
        ss +=1
        if ss > 59:
            ss = 0
            mm+=1
            if mm > 59:
                mm = 0
                hh+=1
    if hh < 10:
        hh = "0"+str(hh)
    hh = str(hh)
    if mm < 10:
        mm = "0"+str(mm)
    mm = str(mm)
    if ss < 10:
        ss="0"+str(ss)
    ss = str(ss)
    time = hh+":"+mm+":"+ss
    return time

        

print(make_readable(459999))