import csv
import mysql.connector
from datetime import datetime

#Creating database connection
mydb=mysql.connector.connect(host="localhost",user="root",port="8080",password="")

#Creating object for performing all operations on database 
mycursor=mydb.cursor()

#Creating database
mycursor.execute("CREATE DATABASE IF NOT EXISTS `pollution-db2`")

#table creation
mycursor.execute("CREATE TABLE IF NOT EXISTS `pollution-db2`.`schema` (`measure` VARCHAR(45)PRIMARY KEY NOT NULL,`desc` VARCHAR(100) NOT NULL,`unit` VARCHAR(35) NOT NULL);")
mycursor.execute("CREATE TABLE IF NOT EXISTS `pollution-db2`.`stations` (site_id INT(11)PRIMARY KEY NOT NULL, `Location` VARCHAR(45)NOT NULL,`geo_point_2d`  VARCHAR(45)NOT NULL);")
mycursor.execute("CREATE TABLE IF NOT EXISTS `pollution-db2`.`readings` (reading_id int(11)PRIMARY KEY NOT NULL AUTO_INCREMENT,datetime datetime NOT NULL,NOx float NULL,NO2 float NULL,NO FLOAT NULL,PM10 float NULL,NVPM10 float NULL,VPM10 float NULL,`NVPM2.5` float NULL,`PM2.5` float NULL,`VPM2.5` float NULL,CO float NULL,O3 float NULL,SO2 float NULL,Temperature float NULL ,RH float NULL,Air_pressure float NULL,DateStart datetime NULL,DateEnd datetime NULL,Current text NULL,`Instrument_Type` varchar(45)NULL,site_id int(11)NULL);")

#Apply Constraints 
mycursor.execute("ALTER TABLE `pollution-db2`.`readings`ADD FOREIGN KEY (`site_id`) REFERENCES `pollution-db2`.`stations` (`site_id`);")

# #Data Insertion for schema table
schema_sql="INSERT INTO `pollution-db2`.`schema`(measure,`desc`,unit) VALUES (%s,%s,%s)"
schema_val= [
        ('Date Time', 'Date and time of measurement','datetime'),
        ('NOx', 'Concentration of oxides of nitrogen','μg/m3'),
        ('NO2', 'Concentration of nitrogen dioxide','μg/m3'),
        ('NO', 'Concentration of nitric oxide','μg/m3'),
        ('SiteID', 'Site ID for the station','integer'),
        ('PM10', 'Concentration of particulate matter <10 micron diameter','μg/m3'),
        ('NVPM10', 'Concentration of non - volatile particulate matter <10 micron diameter','μg/m3'),
        ('VPM10', 'Concentration of volatile particulate matter <10 micron diameter','μg/m3'),
        ('NVPM2.5', 'Concentration of non volatile particulate matter <2.5 micron diameter','μg/m3'),
        ('PM2.5', 'Concentration of particulate matter <2.5 micron diameter','μg/m3'),
        ('VPM2.5', 'Concentration of volatile particulate matter <2.5 micron diameter','μg/m3'),
        ('CO', 'Concentration of carbon monoxide','mg/m3'),
        ('O3', 'Concentration of ozone','μg/m3'),
        ('SO2', 'Concentration of sulphur dioxide','μg/m3'),
        ('Temperature', 'Air temperature','°C'),
        ('RH', 'TRelative Humidity','%'),
        ('Air Pressure', 'Air Pressure','mbar'),
        ('Location', 'Text description of location','text'),
        ('geo_point_2d', 'Latitude and longitude','geo point'),
        ('DateStart', 'The date monitoring started','datetime'),
        ('DateEnd', 'The date monitoring ended','datetime'),
        ('Current', 'Is the monitor currently operating','text'),
        ('Instrument Type', 'Classification of the instrument','text')
        ]
mycursor.executemany(schema_sql,schema_val)
mydb.commit()

#Opening cleaned file for data insertion in stations table
with open('clean.csv', mode ='r')as csv_file:
     reader = csv.reader(csv_file,delimiter=';')

     #Set iteration variable to zero for header
     iteration=0;
     
     #Iterating rows for reader file
     for rows in reader:
          if iteration==0:
             print("Being Processed")
          else:
               #Inserting data from cleaned file in station table
               stations_sql = "INSERT IGNORE INTO `pollution-db2`.`stations` (`site_id`,`Location`,`geo_point_2d`) VALUES (%s, %s,%s)"
               stations_val = ( rows[4],rows[17],rows[18] )
               mycursor.execute(stations_sql, stations_val)
               mydb.commit()
          iteration+=1

     #Set iteration variable to zero for header
     iteration=0;
     
     #Iterating rows for reader file
     for rows in reader:
          if iteration==0:
             print("Being Processed")
          else:
               #Inserting data from cleaned file in readings table
               readings_sql = "INSERT INTO `pollution-db2`.`readings` (`datetime`, NOx,NO2,`NO`,PM10,NVPM10,VPM10,`NVPM2.5`,`PM2.5`,`VPM2.5`,CO,O3,SO2,Temperature,RH,Air_Pressure,DateStart,DateEnd,`Current`,Instrument_Type,site_id) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
               readings_val = (datetime.fromisoformat(rows[0]),rows[1] if rows[1]!="" else None,
                     rows[2] if rows[2]!="" else None,rows[3] if rows[3]!="" else None,
                     rows[5] if rows[5]!="" else None,rows[6] if rows[6]!="" else None,
                     rows[7] if rows[7]!="" else None,rows[8] if rows[8]!="" else None,
                     rows[9] if rows[9]!="" else None,rows[10] if rows[10]!="" else None,
                     rows[11] if rows[11]!="" else None,rows[12] if rows[12]!="" else None,
                     rows[13] if rows[13]!="" else None,rows[14] if rows[14]!="" else None,
                     rows[15] if rows[15]!="" else None,rows[16] if rows[16]!="" else None,
                     datetime.fromisoformat(rows[19]) if rows[19]!="" else None,
                     datetime.fromisoformat(rows[20]) if rows[20]!="" else None,
                     rows[21],rows[22],rows[4])
               mycursor.execute(readings_sql, readings_val)
               mydb.commit()
          iteration+=1
    
     #closing the file clean.csv
     reader.close()
     #Disconnecting from the server
     mydb.close()






    









