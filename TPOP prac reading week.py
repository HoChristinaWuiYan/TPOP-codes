##TPOP practical reading week

##Write a function printBasePattern(n) taking one integer parameter
##representing the size of the pattern to print. The size of the print
##must be greater or equal to 3. If the size is invalid you should print
##an error message (or even better raise an exception).

def printBasePattern(n):
    if n<3:
        raise ValueError
    else:
        x = 0
        y = n-1
        for column in range (n):
            a = ['.']*n
            a[x] = "x"
            a[y] = "x"
            a = (str(a).strip('[]'))
            a = a.replace("', '", '')
            a = a.replace("'", '')
            print (a)
            x = x + 1
            y = y - 1

## Same question as above, except that two additional string parameters
## must be given, each one representing the different character of the
## pattern       
                
def printExtendedBasePattern(n, letter, symbol):
    if n<3:
        raise ValueError
    else:
        x = 0
        y = n-1
        for column in range (n):
            a = [symbol]*n
            a[x] = letter
            a[y] = letter
            a = (str(a).strip('[]'))
            a = a.replace("', '", '')
            a = a.replace("'", '')
            print (a)
            x = x + 1
            y = y - 1           
            

##This time we want to reproduce several times the same pattern.
##Write a function printMultipleBasePattern taking two integer
##parameters, the first one representing the number of rows and
##the second parameter representing the number of columns. The
##pattern should be printed in each cells, e.g. a total of
##rows × columns times. Both parameters must be greater or equal
##to 0. If they are invalid you should print an error message
##(or even better raise an exception).        

def printMultipleBasePattern(row, column):
    if row<0:
        raise ValueError
    if column<0:
        raise ValueError
    else:
        for i in range(row):
            print (("O--O")*column)
            print (("-OO-")*column)
            print (("-OO-")*column)
            print (("O--O")*column)

##Dictionary

decypherbook = {'0000':8, '0001':1, '0010':0, '0011':9, '0100':5,
                '0101':3, '0110':7, '0111':2, '1110':4, '1111':6}
cypherbook1 = {8:'0000', 1:'0001', 0:'0010', 9:'0011', 5:'0100',
              3:'0101', 7:'0110', 2:'0111', 4:'1110', 6:'1111'}
cypherbook2 = {'0000':8, '0001':1, '0010':0, '0011':9, '0100':5,
                '0101':3, '0110':7, '0111':2, '1110':4, '1111':6,
               8:'0000', 1:'0001', 0:'0010', 9:'0011', 5:'0100',
              3:'0101', 7:'0110', 2:'0111', 4:'1110', 6:'1111'}

##We can use the cypherbook dictionary to encode numbers such as 1253495.
##Write a function encode( cyper, number) taking a cypher dictionary and
##a string representing a number as parameters and returned the encoded
##number.
##For example encode(cypherbook, "12") should return "00010111".

def encode(cyper,number):
    number = eval(number)
    number = str(number)
    print ('"', end="")
    for i in number:
        i = eval(i)
        a = cyper [i]
        print (a, end="")
    print('"')


##Same exercise but this time to decode a message. In this case we must
##pass in the parameters the dictionary to be used to decipher the message.
##For example, decode(decypherbook, "00010111") should return "12"

def decode(cyper,number):
    number = str(number)
    a = cyper [number[0:4]]
    b = cyper [number[4:]]
    print ('"', end="")
    print (a, end="")
    print (b, end="")
    print ('"', end="")

##For part i and ii we need to use two dictionaries, one for encoding and one
##for decoding. Write a function such that the same dictionary is used for
##coding and decoding. For example, advanced_decode(cypherbook, "00010111")
##should return "12" and advanced_encoode(cypherbook, "12") should return
##"00010111".

def advancecode (cyper, number):
    if len(number)>2:
        decode(cyper, number)
    else:
        encode(cyper, number)
