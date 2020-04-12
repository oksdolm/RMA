import random
numberTuples = [1000]                 #Number of tuples
numberAttributesApp = [100]          #Number of attributes in application part
numberAttributesDes = [1]       #Number of attributes in descriptive part
shareOrderBy = [0]    #Share of the order part
tries = [1]
randomMIN = 0
randomMAX = 10000
#keep sparsity 0 for all experiments except experiments with sparsity
sparsity = 0
#Specify the folder where this file is located
adressToExperimentFolder  = "/root/QR/README"
#Create List of created files
createdFiles =[]


for attributesDes in  range(len(numberAttributesDes)):
    for attributesApp in  range(len(numberAttributesApp)):
        for orderby in range (len(shareOrderBy)):

	    
            for tuples in range(len(numberTuples)):

                #Define name of the test case
                fileName = '_%sx%sx%s_order%s' %(numberTuples[tuples],numberAttributesDes[attributesDes],numberAttributesApp[attributesApp], shareOrderBy[orderby])
                
                #Define the names of the scripts for the test case
                fileNameCreateIntern = 'Create_Intern%s.sql'%fileName
                fileNameInsertIntern = 'Insert_Intern%s.sql'%fileName
                fileNameSelectIntern = 'Select_Intern%s.sql'%fileName
                fileNameSelectAddIntern = 'Add_Intern%s.sql'%fileName
                fileCreateIntern = open(fileNameCreateIntern,'w+')
                fileInsertIntern = open(fileNameInsertIntern,'w+')
                fileSelectIntern = open(fileNameSelectIntern,'w+')
                fileNameSelectAddIntern = open(fileNameSelectAddIntern,'w+')
        
                #Define table name
                tableName = 'table_%sx%sx%s_order%s' %(numberTuples[tuples],numberAttributesDes[attributesDes],numberAttributesApp[attributesApp], shareOrderBy[orderby])

                
                #Fill Create-File
                #Creation of first table
                fileCreateIntern.write ('CREATE TABLE %s (' %tableName)
                totalNumberAttributes = numberAttributesDes[attributesDes]+numberAttributesApp[attributesApp]
                orderByNumberAttributes = int(numberAttributesDes[attributesDes]*shareOrderBy[orderby]/100)
                for num in range(1,totalNumberAttributes+1):
                    fileCreateIntern.write ('"x%s" double' %num)
                    if num == totalNumberAttributes:
                        fileCreateIntern.write (');\n')
                    else:
                        fileCreateIntern.write (', ')
                #Creation of second table
                fileCreateIntern.write ('CREATE TABLE %s1 (' %tableName)
                totalNumberAttributes = numberAttributesDes[attributesDes]+numberAttributesApp[attributesApp]
                orderByNumberAttributes = int(numberAttributesDes[attributesDes]*shareOrderBy[orderby]/100)
                for num in range(1,totalNumberAttributes+1):
                    fileCreateIntern.write ('"y%s" double' %num)
                    if num == totalNumberAttributes:
                        fileCreateIntern.write (');\n')
                    else:
                        fileCreateIntern.write (', ')

                #Create CSV-File
                fileNameCSV = 'CSV_Intern_%s.csv'%tableName
                fileCSV = open(fileNameCSV,'w+')
                createdFiles.append (fileNameCSV)
                for numY in range(1,numberTuples[tuples]+1):
                    for numX in range(1,totalNumberAttributes+1):
                        a = random.randint(randomMIN,randomMAX)
                        #uncomment next 3 lines for sparsity experiments
                        #if a < randomMAX*sparsity:
                            #fileCSV.write('0')
                        #else:
                        fileCSV.write('%s' %a)
                        if numX == totalNumberAttributes:
                            fileCSV.write (';\n')
                        else:
                            fileCSV.write (';')
                fileCSV.close()
                

                #Fill Insert-File
                fileInsertIntern.write ('COPY %s RECORDS INTO %s FROM \'%s/%s\' USING DELIMITERS \';\',\'\\n\';\n' %(numberTuples[tuples],tableName,adressToExperimentFolder,fileNameCSV))
                fileInsertIntern.write ('COPY %s RECORDS INTO %s1 FROM \'%s/%s\' USING DELIMITERS \';\',\'\\n\';\n' %(numberTuples[tuples],tableName,adressToExperimentFolder,fileNameCSV))


                #Fill Selection files
                for time in range(len(tries)):
                    #many ordering columns, one application column:
                    #QR decomposition
                    #fileSelectIntern.write ('SELECT * FROM LAPACK (%s ON ' %tableName)
                    #fileSelectIntern.write ('SELECT * FROM QQR (%s ON ' %tableName)
                    #fileSelectIntern.write ('x1  ORDER BY ')
                    #for num in range(2,totalNumberAttributes+1):
                        #fileSelectIntern.write ('x%s' %num)
                        #if num == totalNumberAttributes:
                            #fileSelectIntern.write (' );\n ')
                        #else:
                            #fileSelectIntern.write (',')
                            
                    #addition on two tables
                    #fileNameSelectAddIntern.write ('SELECT * FROM (%s ON ' %tableName)
                    #fileNameSelectAddIntern.write ('x1  ORDER BY ')
                    #for num in range(2,totalNumberAttributes+1):
                        #fileNameSelectAddIntern.write ('x%s' %num)
                        #if num == totalNumberAttributes:
                            #fileNameSelectAddIntern.write (' ) ADD (%s1 ON ' %tableName)
                        #else:
                            #fileNameSelectAddIntern.write (',')
                    #fileNameSelectAddIntern.write ('y1  ORDER BY ')
                    #for num in range(2,totalNumberAttributes+1):
                        #fileNameSelectAddIntern.write ('y%s' %num)
                        #if num == totalNumberAttributes:
                            #fileNameSelectAddIntern.write (' );\n ')
                        #else:
                            #fileNameSelectAddIntern.write (',')
                            
                            
                    fileNameSelectAddIntern.write ('SELECT * FROM (%s ON ' %tableName)
                    for num in range(2,totalNumberAttributes+1):
                        fileNameSelectAddIntern.write ('x%s' %num)
                        if num == totalNumberAttributes:
                            fileNameSelectAddIntern.write (' ORDER BY x1) ADD (%s1 ON ' %tableName)
                        else:
                            fileNameSelectAddIntern.write (',')
                    for num in range(2,totalNumberAttributes+1):
                        fileNameSelectAddIntern.write ('y%s' %num)
                        if num == totalNumberAttributes:
                            fileNameSelectAddIntern.write (' ORDER BY y1);\n ')
                        else:
                            fileNameSelectAddIntern.write (',')       
                    
                    
                    #many application columns, one ordering column:
                    #fileSelectIntern.write ('SELECT * FROM LAPACK (%s ON ' %tableName)
                    fileSelectIntern.write ('SELECT * FROM QQR (%s ON ' %tableName)
                    for num in range(2,totalNumberAttributes+1):
                        fileSelectIntern.write ('x%s' %num)
                        if num == totalNumberAttributes:
                            fileSelectIntern.write (' ORDER BY ')
                        else:
                            fileSelectIntern.write (',')
                    fileSelectIntern.write ('x1);\n')    
                    


                #Fill Delete-File
                #fileDeleteIntern.write ('DROP TABLE %s;\n\n' %tableName)
                #print('Table %s generated' %tableName)
                    
                fileCreateIntern.close()
                fileInsertIntern.close()
                fileSelectIntern.close()
                fileNameSelectAddIntern.close()
