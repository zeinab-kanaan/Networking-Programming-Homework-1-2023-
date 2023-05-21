L=['Network','Math','Programming','Physsics','Music']
p = []
for i in L:
    x=i.startswith('Ph')
    if x== True:
        p.append(i)
print(p)