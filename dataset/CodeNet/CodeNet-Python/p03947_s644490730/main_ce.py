s="BBBWW"
now=s[0]
ans=0
for i in xrange(1,len(s)):
    if now!=s[i]:
        ans+=1
        now=s[i]
print ans
