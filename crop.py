import csv
from datetime import datetime

#Opening file for writing data
with open('crop.csv', 'w') as csvfile_writer:
    writer = csv.writer(csvfile_writer, delimiter=';')

    #Opening CSV file for reading data
    with open('bristol-air-quality-data.csv','r') as csvfile_reader:
        reader=csv.reader(csvfile_reader,delimiter=';')

        #Set iteration variable to zero for header
        iteration=0

        #Iterating rows for reader file
        for rows in reader:
            if iteration==0:
                #Printing Header row
                writer.writerow(rows)
            else:
                   if rows[0]!="":
                      if datetime.fromisoformat(rows[0])>=datetime.fromisoformat('2010-01-01T00:00:00+00:00') :
                          #print rows  after  1 Jan 2010
                          writer.writerow(rows)
            iteration+=1
        #Closing reader file
        csvfile_reader.close()
        #Closing writer file
        csvfile_writer.close()