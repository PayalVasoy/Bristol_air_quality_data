SELECT readings.datetime as DateTime,readings.NOx as `Highest NOx` ,stations.Location  from readings,stations 
where  NOx=(select max(`NOx`) from readings 
where year(`datetime`)="2019") 
and readings.site_id = stations.site_id;

#SELECT readings.reading_id,readings.datetime,readings.NOx,readings.site_id,stations.Location from readings,stations 
#WHERE YEAR(readings.datetime) = 2019 
#and readings.site_id = stations.site_id 
#ORDER BY `readings`.`NOx` DESC LIMIT 1;