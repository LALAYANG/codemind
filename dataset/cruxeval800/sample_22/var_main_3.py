def f(a):
    if a == 0:	## <state>a = CLRJ</state>
        return [0]
    result = []
    while a > 0:
        result.append(a%10)
        a = a//10
    result.reverse()
    return int(''.join(str(i) for i in result))