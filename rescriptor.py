__author__ = 'student'
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
global D
D = {}
D['а'] = 7.5
D['б'] = 1.7
D['в'] = 4.6
D['г'] = 1.6
D['д'] = 3
D['е'] = 8.8
D['ж'] = 0.8
D['з'] = 1.9
D['и'] = 7.5
D['й'] = 1.2
D['к'] = 3.4
D['л'] = 4.2
D['м'] = 3.2
D['н'] = 6.4
D['о'] = 10.9
D['п'] = 2.8
D['р'] = 4.8
D['с'] = 5.4
D['т'] = 6.4
D['у'] = 2.6
D['ф'] = 0.2
D['х'] = 1.1
D['ц'] = 0.5
D['ч'] = 1.5
D['ш'] = 0.7
D['щ'] = 0.4
D['ы'] = 1.9
D['ь'] = 1.7
D['э'] = 0.4
D['ю'] = 0.7
D['я'] = 2.2
R={}
R['а'] = 0
R['б'] = 0
R['в'] = 0
R['г'] = 0
R['д'] = 0
R['е'] = 0
R['ж'] = 0
R['з'] = 0
R['и'] = 0
R['й'] = 0
R['к'] = 0
R['л'] = 0
R['м'] = 0
R['н'] = 0
R['о'] = 0
R['п'] = 0
R['р'] = 0
R['с'] = 0
R['т'] = 0
R['у'] = 0
R['ф'] = 0
R['х'] = 0
R['ц'] = 0
R['ч'] = 0
R['ш'] = 0
R['щ'] = 0
R['ы'] = 0
R['ь'] = 0
R['э'] = 0
R['ю'] = 0
R['я'] = 0
keytable = {}
line = input()
line = line.lower()
k = 0
for i in range(len(line)):
    if line[i]>='а' and line[i]<='я':
        k+=1
print(k)
for i in range(len(line)):
    if line[i]>='а' and line[i]<='я' and line[i] in R:
        R[line[i]]+=1
for key in R.keys():
    R[key] = round(R[key]/k*100,1)
for key in D.keys():
    keytable[key] = 0
d = [0]*31
r = [0]*31
i=0
for key in D.keys():
    d[i] = D[key]
    i+=1
d=sorted(d)
i=0
for key in R.keys():
    r[i] = R[key]
    i+=1
r=sorted(r)
for j in range(len(d)):
    for key in D.keys():
        if D[key] == d[j]:
            l = key
            z = r[j]
            for meow in R.keys():
                if R[meow] ==z:
                    f = meow
            keytable[l] = f
translate=''
for i in range(len(line)):
    if line[i] in keytable:
        translate+=keytable[line[i]]
    else:
        translate+=line[i]
print(D)
print(d)
print(R)
print(r)
print(keytable)
print(translate)