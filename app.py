from flask import Flask
from flask import request
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS


app = Flask(__name__)



@app.route("/api/humidity", methods=['POST'])
def humiditySensors():
    if request.method == 'POST' :

        data = request.data        
        transformOne = str(data).split(":")
        transgormTwo = transformOne[1].split("\"")
        payload = transgormTwo[1]

        legnth = len(payload)

        if legnth == 6 :
            print(payload[2:6])
            res =  int(payload[2:6], 16)
            result = int(res) / 10
            writes("humidity", result)
        elif legnth == 10 :
            print(payload[2:6])
            print(payload[7:10])
            res =  int(payload[7:10], 16)
            result = int(res) / 10
            writes("humidity", result)
     

        return request.data

    

@app.route("/api/temperature", methods=['POST'])
def temperatureSensors():
    if request.method == 'POST' :

        data = request.data        
        transformOne = str(data).split(":")
        transgormTwo = transformOne[1].split("\"")
        payload = transgormTwo[1]

        legnth = len(payload)
        

        if legnth == 6 :
            print(payload[2:6])
            res =  int(payload[2:6], 16)
            result = int(res) / 10
            writes("temperature", result)
        elif legnth == 10 :
            print(payload[2:6])
            print(payload[7:10])
            res =  int(payload[7:10], 16)
            result = int(res) / 10
            writes("temperature", result)


        
   
        return request.data



    
def writes(name, value):
    bucket = "keyce"
    org = "keyce"
    token = "4nc7Spb327W37-1iSykbPm8zB8nlCncPVLMBbUoypHMiMDVrU6FLj2klg6u1A--4BkUy_4H1BHGVYqkFQEEwUQ=="

    url="http://localhost:8086"

    client = influxdb_client.InfluxDBClient(
       url=url,
       token=token,
       org=org
    )


    write_api = client.write_api(write_options=SYNCHRONOUS)

    p = influxdb_client.Point("mesure").field(name, value)
    write_api.write(bucket=bucket, org=org, record=p)