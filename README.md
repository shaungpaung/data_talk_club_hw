# data_talk_club_hw

Task 3:

docker build -t int_data:v001 .
URL="http://192.168.100.59:8000/green_tripdata_2019-10.csv.gz"
docker run -it \
    --network=hw_1_default \
    data_int:v_1 \
    --user=postgres \
    --password=postgres \
    --host=db \z
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url=${URL}