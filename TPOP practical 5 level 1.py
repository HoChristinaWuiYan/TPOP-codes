##TPOP practical 5 Level 1
##
##
##Q1)
##output_file = open ("exo1.txt", "w")
##output_file.write ("a_word")
##output_file.close()
##
##read_file = open("exo1.txt", "r")
##print(read_file.read())


##Q2)
####
##def saveListToFile (sentences, filename):
##    a = open(filename, "w")
##    for i in range (len(sentences)):
##        a.write(sentences[i])
##        a.write('\n')
##    a.close()
##
##    read_file = open(filename, "r")
##    print(read_file.read())
##
##saveListToFile(['hello', 'world'], "filename")
####      
##

##Q3)
##
##def saveToLog(entry, logfile):
##    with open(logfile, "a") as myfile:
##        myfile.write(entry+"\n")
##        
##logfile = open ("logfile", "a")
####logfile.write("I Love Coding Rubbish")
##logfile.write('\n')
##logfile.close()
##
##read_file = open("logfile", "r")
##print(read_file.read())
##
##saveToLog("Hahaa", 'logfile')


##Q4
##def saveToLog(entry, logfile):
##    entry = entry.upper()
##    with open(logfile, "a") as myfile:
##        myfile.write(entry+"\n")
##        
##logfile = open ("logfile", "a")
##logfile.write("I Love Coding Rubbish")
##logfile.write('\n')
##logfile.close()
##
##read_file = open("logfile", "r")
##print(read_file.read())
##
##saveToLog("Hahaa", 'logfile')

##Q5
##def toUpperCase(input_file, output_file):
##    input_file = open ("abcdefg", "w")
##    input_file.write ("write_sth")
##    input_file.close()
##    
##    read_file = open("abcdefg", "r")
##    print(read_file.read())
##
##    with open("abcdefg", "a") as output_file:
##

##################################################
##def toUpperCase(input_file, output_file):
##    data = []
##    in_file = open(input_file, 'r')
##    for line in in_file:
##        data.append(line)
##
##    out_file = open(output_file, 'w')
##    for element in data:
##        out_file.write(element.upper() + '\n')
##
##toUpperCase("logfile", "logfile2")


##Q6
##def sumFromFile(filename):
input_file = open ("abcdefg", "w")
input_file.write ("write_sth")
input_file.close()
   

