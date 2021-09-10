numerostupla= (13, 1, 8, 3, 2, 5, 8)
listan=[]
for i in numerostupla:
    if i<5:
        listan.append(i)
    else:
        continue
else:
    print("Fin For")
    print(listan)