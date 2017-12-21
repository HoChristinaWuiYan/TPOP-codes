Tpop prac 3

def power4(a):
    b=(a**4)
    print (b)
def addsquare(a,b):
    c=((a+b)**2)
    return (c)
userinput=int(input("please enter a number"))
userinput2=int(input("please enter another number"))
answer=addsquare(userinput,userinput2)
print(answer)



def question1():

    a = str(input("What word do you want to check? "))
    a = a.lower()
    a = a.replace(" ", "")
    b = a[::-1]
    if a==b:
        print ("YES Its a palindromeeee")
    else:
        print ("NO Its not a palindromeeee")

question1



vectorinput = [3, 4, 5]
for i in range (3):
    vectorinput[i]=float(input("Please put in your value of your vector"))
print (vectorinput)
scalarinput = float(input("PLease enter your scalar factor"))

for i in range (3):
    vectorinput[i]= vectorinput[i]*scalarinput
print (vectorinput)


#vectorinput = [3, 4, 5]
#for i in range (3):
#    vectorinput[i]=float(input("Please put in your value of your vector"))
#print (vectorinput)

#vectorinput2 = [3, 4, 5]
#for i in range (3):
#    vectorinput2[i]=float(input("Please put in your value of your vector"))
#print (vectorinput2)

#for i in range (3):
#    vectorinput[i]= vectorinput[i]+vectorinput2[i]
#print (vectorinput)




word = list(str(input("Please enter a word")))
question = input("Do you want your word encrypt or decrypt?")
shift = int(input("Please enter your shift for your word"))

def caesar_encrypt(abc, d):
    for i in range (len(abc)):
        if abc[i]==(" "):
            abc[i] = abc[i]
        else:
            new = ord(abc[i])+d
            if new>122:
                new=new-26
                abc[i] = chr(new)
            else:
                abc[i] = chr(new)
    abc=''.join(abc)
    print (abc)

def caesar_decrypt(abc, d):
    for i in range(len(abc)):
        if abc[i] == (" "):
            abc[i] = abc[i]
        else:
            new = ord(abc[i]) - d
            if new > 122:
                new = new + 26
                abc[i] = chr(new)
            else:
                abc[i] = chr(new)
    abc = ''.join(abc)
    print(abc)

if question== "encrypt":
    caesar_encrypt(word,shift)
else:
    caesar_decrypt(word, shift)

