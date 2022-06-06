
import csv

#Opening cleaned file for reading data
with open('clean.csv','r')as csv_file:
    reader=csv.reader(csv_file,delimiter=';')

    #Opening sql file for writing data from cleaned file
    with open('insert-100.sql','w')as sql_file:

        #Set variable values for looping and conditions
        iteration=0
        start_limit=0
        record_limit=100

        #Iterating rows for reader file
        for rows in reader:
            if start_limit<=record_limit:
                if iteration==0:

                    #Header printing
                    header=("Date time, NOx,NO2,NO,PM10,NVPM10,VPM10,NVPM2.5,PM2.5,VPM2.5,CO,O3,SO2,Temperature,RH,Air_Pressure,DateStart,DateEnd,Current,Instrument_Type,SiteId")
                    sql_file.write(header+"\n")
                else:

                    #Writing data in sql file
                    data=(rows[0],rows[1] if rows[1]!="" else None,
                          rows[2] if rows[2]!="" else None,
                          rows[3] if rows[3]!="" else None,
                          rows[5] if rows[5]!="" else None,
                          rows[6] if rows[6]!="" else None,
                          rows[7] if rows[7]!="" else None,
                          rows[8] if rows[8]!="" else None,
                          rows[9] if rows[9]!="" else None,
                          rows[10] if rows[10]!="" else None,
                          rows[11] if rows[11]!="" else None,
                          rows[12] if rows[12]!="" else None,
                          rows[13] if rows[13]!="" else None,
                          rows[14] if rows[14]!="" else None,
                          rows[15] if rows[15]!="" else None,
                          rows[16] if rows[16]!="" else None,
                          rows[19] if rows[19]!="" else None,
                          rows[20] if rows[20]!="" else None,
                          rows[21],rows[22],rows[4])
                    sql_file.write(str(data)+"\n")
                iteration+=1
            start_limit+=1

     
    