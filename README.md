# data_talk_club_hw
##Home Work 1
Task 1:
pip --version
Ans is 24.3.1

Task 2:
Ans is db:5433

Task 3:
SELECT 
    SUM(CASE WHEN trip_distance <= 1 THEN 1 ELSE 0 END) AS "Up to 1 mile",
    SUM(CASE WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1 ELSE 0 END) AS "1-3 miles",
    SUM(CASE WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1 ELSE 0 END) AS "3-7 miles",
    SUM(CASE WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1 ELSE 0 END) AS "7-10 miles",
    SUM(CASE WHEN trip_distance > 10 THEN 1 ELSE 0 END) AS "Over 10 miles"
FROM green_trip_data
WHERE 
    lpep_pickup_datetime >= '2019-10-01' 
    AND lpep_pickup_datetime < '2019-11-01';

Ans is 104830	198995	109642	27686	35201


Task 4:

WITH DailyMax AS (
    SELECT 
        DATE(lpep_pickup_datetime) AS pickup_date,
        MAX(trip_distance) AS max_distance
    FROM green_trip_data
    WHERE 
        lpep_pickup_datetime >= '2019-10-01' 
        AND lpep_pickup_datetime < '2019-11-01'
    GROUP BY DATE(lpep_pickup_datetime)
)
SELECT 
    pickup_date,
    max_distance
FROM DailyMax
ORDER BY max_distance DESC
LIMIT 1;

Ans is "2019-10-31"	515.89

Task 5:

SELECT 
    g."PULocationID",
    z."Zone",
    z."Borough",
    SUM(g.total_amount) AS total_revenue
FROM 
    green_trip_data g
JOIN 
    taxi_zone z
ON 
    g."PULocationID" = z."LocationID"
WHERE 
    DATE(g.lpep_pickup_datetime) = '2019-10-18'
GROUP BY 
    g."PULocationID", z."Zone", z."Borough"
HAVING 
    SUM(g.total_amount) > 13000
ORDER BY 
    total_revenue DESC
LIMIT 3;

Ans  is 74	"East Harlem North"	"Manhattan"	18686.68000000005
        75	"East Harlem South"	"Manhattan"	16797.260000000064
        166	"Morningside Heights"	"Manhattan"	13029.790000000034


Task 6:

SELECT 
    z2."Zone" AS dropoff_zone,
    MAX(g.tip_amount) AS largest_tip
FROM 
    green_trip_data g
JOIN 
    taxi_zone z1 ON g."PULocationID" = z1."LocationID"
JOIN 
    taxi_zone z2 ON g."DOLocationID" = z2."LocationID"
WHERE 
    z1."Zone" = 'East Harlem North'
    AND g.lpep_pickup_datetime BETWEEN '2019-10-01' AND '2019-11-01'
GROUP BY 
    z2."Zone"
ORDER BY 
    largest_tip DESC
LIMIT 1;

Ans is "JFK Airport"	87.3

Task 7: