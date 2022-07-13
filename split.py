t=int(input('no ' ))
for i in range(t):
    w,x,y,z=map(int,input('enter'   ).split())
    print(w)
    b=w+(y*z)
    if b>x:
        print("OVERFLOW")
    elif b==x:
        print("Filled")
    else:
        print("UNFILLED")


