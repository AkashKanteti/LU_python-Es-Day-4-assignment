mess='what we think we become;we are Python programmer'
i=0
lis=list()
while True:
    if 'we' in mess[i:]:
        k=mess[i:].find('we')
        i+=k+1
        lis.append(i-1)
    else:
        break
print(lis)
