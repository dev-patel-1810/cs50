# A basic cs50 question where we take the input from the user be it name or something till the person enters EOF command(Ctrl + c) which will return the user in the format of "Adieu, adieu, to " and the names entered by the user.
c=0
l=[]
a=" "
try:
    while a!='':
        c=c+1
        a=input("")

        l.append(a)
except:
    # print(l)
    print("Adieu, adieu, to ",end='')
    for i in range(len(l)):
        if i==0:
            print(l[i] ,end='')
        elif i==c-2:
            if i==1:
                print(" and " + l[i])
            else:
                print(", and " + l[i])
        elif i<c-2:
            print(", "+ l[i] , end='')

