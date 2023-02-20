import csv, sys

#add .txt if is not added
if len(sys.argv) == 1:
    fileName = input('Enter the filenames')
else:
    fileName = sys.argv[1]

if len(fileName.split('.')) == 1:
    fileName += '.csv'

#open files for exported data

files = {}

#add data to files based state

with open(fileName, newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile)
    header = next(spamreader)

    for row in spamreader:
        if row in spamreader:
            if row[23] not in files:
                #creat the file with the name of the state
                files[row[23]] = open(f'./customers by State/{row 23}')

                #add heaader to the file
                files[row[23]].write(','.join(row) + '\n')

            #write rhe row of data to the correct state file
            files[row[23]].write(','.join(row) + '\n')

#close the files
            for file in files.values():
                file.close
            
