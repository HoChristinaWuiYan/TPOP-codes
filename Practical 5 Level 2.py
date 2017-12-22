##Practical 5
##Question 1
##try:
##    dataFile = open('Data/precipitations-europe.txt')
##except IOError as err:
##    print ('The following error occurred:',err)
##else:
##    data = dataFile.readlines()
##    dataFile.close() # we have read the full content of the file so we can close it
##    minPrecipitation = []
##    maxPrecipitation = []
##    averagePrecipitation = 0.0
##    row = 1 # first line should be omitted
##
##    while row < len(data):
##        
##        cells = data[row].split(',')
##        cells[0] = int(cells[0])
##        cells[1] = float(cells[1])
##        if (len(minPrecipitation) == 0 or
##            cells[1] < minPrecipitation[1]):
##            minPrecipitation = [cells[0], cells[1]]
##
##        if (len(maxPrecipitation) == 0  or
##            cells[1] > maxPrecipitation[1]):
##            maxPrecipitation = [cells[0], cells[1]]
##            
##        averagePrecipitation += cells[1]
##
##        row += 1
##        
##    print ("min precipitation was", minPrecipitation[1], end='')
##    print (" and it occurred in",minPrecipitation[0],)
##    
##    print ("max precipitation was", maxPrecipitation[1], end='')
##    print (" and it occurred in",maxPrecipitation[0])
##        
##    print ("the average precipitation in last century was",
##           averagePrecipitation/(len(data)-1))


##Question 2.1
##dataRecords = {}    # keys are years, value are list of three floats:
##                    # precipitation for Europe, NAmerica, World
##listOfFiles = ['precipitations-europe.txt',
##               'precipitations-NAmerica.txt',
##               'precipitations-world.txt']
##validListOfFiles = []
##
##for fileName in listOfFiles:
##    try:
##        dataFile = open(fileName)
##    except IOError as err:
##        print ('The following error occurred:',err)
##    else:
##        validListOfFiles.append(fileName)
##        data = dataFile.readlines()
##        dataFile.close()
##        row = 1 # first line should be ommitted
##        while row < len(data):
##            
##            cells = data[row].split(',')
##
##            # convert each cell to its appropriate type rather than keeping
##            # all cells as string
##            cells[0] = int(cells[0])
##            cells[1] = float(cells[1])
##            if cells[0] in dataRecords:
##                dataRecords[cells[0]].append(cells[1])
##            else:
##                # must create a list containing a single element
##                dataRecords[cells[0]] = [cells[1]]
##
##            row += 1
##
##
#### This section of the code deals with writing the collated data to
#### a text file (.CSV)
##try:
##    outputFile = open('collatedFiles.txt','w')
##except IOError as err:
##    print ('The following error occurred:',err)
##else:
##    # write the header of the file, e.g. column names
##    outputFile.write('Years,')
##    outputFile.write(','.join(validListOfFiles))
##    outputFile.write('\n')
##    outputFile.flush()
##
##    # write the data. item is a tuple containing item[0]: the key (e.g. year)
##    # and item[1] the list of values (three in this case) corresponding the
##    # precipitation for that particular year.
##    for item in sorted(dataRecords.items()):
##        outputFile.write(str(item[0]))
##        for value in item[1]:
##            outputFile.write(',')
##            outputFile.write(str(value))
##        outputFile.write('\n')
##        outputFile.flush()
##
##    outputFile.close()


##Question 2.2
##def readDataFile(fileName):
##    try:
##        dataFile = open(fileName)
##    except IOError as err:
##        print ('The following error occurred:',err)
##        raise   # We don't want to deal with the error here
##                # We let the calling function deal with it.
##    else:
##        data = dataFile.readlines()
##        dataRecords = {}
##        dataFile.close()
##        row = 1 # first line should be ommitted
##        while row < len(data):
##            
##            cells = data[row].split(',')
##            if cells[0] in dataRecords:
##                raise ValueError() # there should not be duplicate year in the file
##            else:
##                dataRecords[int(cells[0])] = float(cells[1])
##
##            row += 1
##        return dataRecords
##    
##
##
##def collatePrecipitationFile(fileNames,outputFile):
##    '''
##    Collate the data of all the files where the name is in the list of string
##    fileNames and store the collated data in the file whose name is given by
##    the parameter outputfile (a string). files that cannot be opened are simply
##    ignored. It is assumed that the data in each file is correct and complete,
##    e.g. all contains the same years. Note no checking is done regarding the
##    validity of the data.
##    The data is written as a CSV file.
##    
##    '''
##    listDataRecords = {}    # keys are years, value are list of three floats:
##                    # precipitation for Europe, NAmerica, World or whatever the 
##                    # files past in parameters
##    validListOfFiles = []
##    for name in fileNames:
##        try:
##            dataRecords = readDataFile(name)
##        except IOError as err:
##            print ('The following error occurred:',err)
##        except ValueError as err:
##            print ("duplicate year in file", name)
##        else:
##            validListOfFiles.append(name)
##            for item in dataRecords.items():
##                if item[0] in listDataRecords:
##                    listDataRecords[item[0]].append(item[1])
##                else:
##                    listDataRecords[item[0]] = [item[1]]
##
##    ## This section of the code deals with writing the collated data to
##    ## a text file (.CSV)
##    outputF = open(outputFile,'w')
##    # write the header of the file, e.g. column names
##    outputF.write('Years,')
##    outputF.write(','.join(validListOfFiles))
##    outputF.write('\n')
##    outputF.flush()
##
##    # write the data. item is a tuple containing item[0]: the key (e.g. year)
##    # and item[1] the list of values (three in this case) corresponding the
##    # precipitation for that particular year.
##    for item in sorted(listDataRecords.items()):
##        outputF.write(str(item[0]))
##        for value in item[1]:
##            outputF.write(',')
##            outputF.write(str(value))
##        outputF.write('\n')
##        outputF.flush()
##
##    outputF.close()
##
##
##
############################################
####      TESTS
###########################################
##
##    
##listOfFiles = ['Data/precipitations-europe.txt',
##           'Data/precipitations-NAmerica.txt',
##           'Data/precipitations-world.txt']
##
##collatePrecipitationFile(listOfFiles, 'Data/collated.txt')


##Question 3
### IN THIS MODEL ANSWER, WE ARE USING A SCRIPT, TRY TO TRANSFORM THE SCRIPT
### INTO ONE OR MORE FUNCTION. DISCUSS WITH ONE OF YOUR PEER YOUR SOLUTION,
### ESPECIALLY HOW MANY FUNCTIONS WOULD YOU USE, WHAT EACH FUNCTION SHOULD DO,
### WHAT ARE THE PARAMETERS AND RETURNED VALUES IF ANY.
###
### ANOTHER IMPROVEMENT IS TO WRITE THE DATA LIKE 971.4000000000001 AS 971.4. 
### SEARCH HOW TO FORMAT A STRING BEFORE WRITING THE STRING INTO A FILE.
##
############  READING THE DATA FROM FILE ###########
##
##dataFile = open('Data/aberporth_meteorological_data.txt')
##data = dataFile.readlines()
##dataFile.close()
##
##row = 2 # data starts at row 2 (third row)
##yearRecord = {} #keys are years, values are the list of attribute [frost, rain, sunshine]
##
##while row < len(data):
##    
##    cells = data[row].split(',')
##    if cells[0] in yearRecord:
##        record = yearRecord.get(cells[0])
##        for index in range(4, len(cells)): # 4 as the data we are interested in is in the 5th-7th columns
##            record[index - 4] += float(cells[index]) # -4 is the offset for the indices
##    else:
##        record = []
##        for index in range(4, len(cells)):
##            record.append(float(cells[index]))
##
##        yearRecord[cells[0]] = record
##
##    row += 1
##
##
######## WRITING THE SUMMARY FILE ########
##summaryDataFile = open('Data/aberporth_meteorological_data_summary.txt','w')
##
##summaryDataFile.write(data[0])
##cells = data[1].split(',')
##cells = [cells[0]] + cells[4:] # append the header of each column
##summaryDataFile.write(','.join(cells))
##summaryDataFile.flush()
##
##for item in sorted(yearRecord.items()):
##    line = item[0]
##    for value in item[1]:
##        line += ',' +str(value)
##            
##    summaryDataFile.write(line)
##    summaryDataFile.write('\n')
##    summaryDataFile.flush()
##
##
##summaryDataFile.close()
##
