text = 'csharp'
t = 5
tab = []
for i in text:
    if i.lower() in 'aeiouy':
        tab.append(i.upper() * t)
    else:
        tab.append(i * t)
print(' '.join(tab))