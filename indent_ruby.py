a=''
while True:
    try:
        s=input()
        if(s==''):
            break
        a+=s+'\n'
    except:
        break
print(a.replace('  ',' '))
