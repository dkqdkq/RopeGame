#x = 분자 y=분모
def rule_A(x,y):
    x = y+x
    return check(x,y)

def rule_B(x,y):
    s = x
    x = y*-1
    y = s
    return check(x,y)

def check(x,y):
    if y < 0:
        y *= -1
        x *= -1
    return x,y
