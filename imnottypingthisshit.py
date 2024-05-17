def a():
    o=[]
    for h in range(1,100000):
        o.append(f"    elif j == {h}:")
        if h%2==0:
            o.append("        return 'even'")
        else:
            o.append("        return 'odd'")
    l=["def check_odd_even(j):","    if j == 0:","        return 'even'"]
    return "\n".join(l+o[1:])
def b(c):
    x=a()
    with open(c,'w') as g:
        g.write(x)
b("f")
