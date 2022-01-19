def expanding(a):
    c=len(a)
    lst=[]
    for i in range(c-1):
        d=a[i]-a[i+1]
        lst.append(abs(d))
    if lst==sorted(lst):
        return True
    else:
        return False
a=eval(input())
out=expanding(a)
print(out)
