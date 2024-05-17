def o():
    ዐ=[]
    for Ø in range(1,100000):
        ዐ.append(f"    elif j == {h}:")
        if Ø%2==0:
            ዐ.append("        return 'even'")
        else:
            ዐ.append("        return 'odd'")
    օ=["def check_odd_even(j):","    if j == 0:","        return 'even'"]
    return "\n".join(օ+ዐ[1:])
def О(ó):
    ö=o()
    with open(ó,'w') as о:
        о.write(ö)
О("f")
