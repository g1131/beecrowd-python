i=0
par=0
impar=0
pos=0
neg=0
while i<5:
    y=int(input())
    i+=1
    if y%2==0:
        par+=1
    else:
        impar+=1
 
    if y>0:
        pos+=1
    elif y<0:
        neg+=1

    if i>4:
        break
print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))