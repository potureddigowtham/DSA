def done(s):
    f = {}
    for i in s:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    
    maxi = 0
    val = ""
    for i, j in f.items():
        if j > maxi: 
            maxi = j 
            val = i
    return val

print(done("zmszeqxllzvheqwrofgcuntypejcxovtaqbnqyqlmrwitc"))