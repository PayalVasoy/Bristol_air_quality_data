SELECT readings.site_id,stations.Location,AVG(`PM2.5`),AVG(`VPM2.5`) FROM `readings`,`stations` 
WHERE readings.site_id = stations.site_id 
AND YEAR(readings.datetime) = 2019 
AND HOUR(readings.datetime) ='08:00:00'
GROUP BY readings.site_id;