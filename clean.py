import csv   

#Creating a dataset of station data
dataset = {188:'AURN Bristol Centre',203:'Brislington Depot',206:'Rupert Street',209:'IKEA M32',213:'Old Market',215:'Parson Street School',228:'Temple Meads Station',270:'Wells Road',271:'Trailer Portway P&R',375:'Newfoundland Road Police Station',395:"Shiner's Garage",452:'AURN St Pauls',447:'Bath Road',459:'Cheltenham Road \ Station Road',463:'Fishponds Road',481:'CREATE Centre Roof',500:'Temple Way',501:'Colston Avenue'}

#Opening file for data writing
with open('clean.csv', 'w') as csvfile_writer:
    writer = csv.writer(csvfile_writer, delimiter=';')
    
    #Opening croped file for data reading
    with open('crop.csv','r') as csvfile_reader:
        reader=csv.reader(csvfile_reader,delimiter=';')

        #Set iteration variable to zero
        iteration=0;

        #Iterating reader file
        for rows in reader:
            if iteration==0:
                #Printing Header row
                writer.writerow(rows)
            else:
                #Checking siteid and location are null or not null
                if rows[4]!="" and rows[17]!="":
                    station_id=rows[4]
                    cast_station_id=int(station_id)

                    #Comparing  siteid with station
                    if dataset[cast_station_id]==rows[17]:
                        writer.writerow(rows)
                    else:
                        print("Line Number Which Is Blank: "+str(iteration)+" And stationid: "+rows[4]+ 'And Location: '+rows[17])
                else:
                    print("Line Number Which Is Blank: "+str(iteration)+"  And stationid: "+rows[4]+'And Location: '+rows[17])
            iteration=iteration+1
        #Closing reader file
        csvfile_reader.close()
        #Closing writer file
        csvfile_writer.close()



