m=int(input('Enter an integer as month m:'))
d=int(input('Enter an integer as day d:'))

if (m==3) and (d>=20 and d<=31):
    print ('True')
elif (m==4) and (d>=1 and d<=30):
    print ('True')
elif (m==5) and (d>=1 and d<=31):
    print ('True')
elif (m==6) and (d>=1 and d<=20):
    print ('True')
else:
    print ('Fals')
