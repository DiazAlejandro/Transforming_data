import csv

def break_up_datetime(str):
    list = str.split(' ')
    return list

nombre_archivo = "C:/Users/aleja/Desktop/yellow_tripdata_2019-01.csv"
with open(nombre_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    # Omitir el encabezado
    next(lector, None)
    rows = 0
    outfile = 'data.csv'
    with open(outfile, 'ab') as csvfile:

        for fila in lector:
            vendor_id = fila[0]
            tpep_pickup_datetime = fila[1]
            tpep_dropoff_datetime = fila[2]
            passenger_count = fila[3]
            trip_distance = fila[4]
            ratecode_id = fila[5]
            store_and_fwd_flag = fila[6]
            pu_location_id = fila[7]
            do_location_id = fila[8]
            payment_type = fila[9]
            fare_amount = fila[10]
            extra = fila[11]
            mta_tax = fila[12]
            tip_amount = fila[13]
            tolls_amount = fila[14]
            improvement_surcharge = fila[15]
            total_amount = fila[16]
            congestion_surcharge = fila[17]
            co_sur = ''
            if (congestion_surcharge == ''):
                co_sur = '00.00'
            else:
                co_sur = congestion_surcharge

            str = ","+vendor_id+","+break_up_datetime(tpep_pickup_datetime)[0]+","+break_up_datetime(tpep_pickup_datetime)[1]+","+break_up_datetime(tpep_dropoff_datetime)[0]+","+break_up_datetime(tpep_dropoff_datetime)[1]+","+passenger_count+","+trip_distance+","+ratecode_id+","+store_and_fwd_flag+","+pu_location_id+","+do_location_id+","+payment_type+","+fare_amount+","+extra+","+mta_tax+","+tip_amount+","+tolls_amount+","+improvement_surcharge+","+total_amount+","+co_sur+",\n"
            csvfile.write(str.encode())
            print(rows)
            rows = rows+1
