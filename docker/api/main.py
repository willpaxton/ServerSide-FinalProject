from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import psutil
import platform
from datetime import datetime

import math

import psycopg2

app = FastAPI()

conn = psycopg2.connect(database="database",
                        host="db",
                        user="postgres",
                        password="password",
                        port="5432")



# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World (v2)"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

@app.get("/system_info")
def read_cpu():
    svmem = psutil.virtual_memory()


    return {"total_cpu" : f"{psutil.cpu_percent()}",
            "total_memory" : f"{round(svmem.total/1000000000,1)}GB",
            "percent_memory" : f"{svmem.percent}"}

@app.get("/server_latencies")
def server_latency():



    api_resp = {}

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "servers"');
    servers = cursor.fetchall()

    for x in servers:
        resp = cursor.execute(f"""SELECT * FROM "latencies" WHERE "server_name" = '{x[0]}' LIMIT 60""");
        print(resp)
        data = cursor.fetchall()
        
        api_resp[x[0]] = {}
    

        for y in range(0, len(data)):
            name = data[y][0]
            date = data[y][1]
            ping = data[y][2]

            api_resp[x[0]][y] = {"name" : name,
                            "time" : date,
                            "ping" : ping}

    return api_resp
    # pinging OW US Central
    

# for later use, this could probably be set up in a loop or something

@app.get("/ow-central")
def ow_central():
    cursor = conn.cursor()
    resp = cursor.execute(f"""SELECT latency FROM "latencies" WHERE "server_name" = 'ow-central'""");
    print(resp)
    latency = cursor.fetchall()

    final_latency = []

    for x in latency:
        final_latency.append(x[0])

    resp = cursor.execute(f"""SELECT time FROM "latencies" WHERE "server_name" = 'ow-central'""");
    time = cursor.fetchall()

    final_time = []

    for x in time:
        final_time.append(x[0])

    data = {"latency":final_latency,
            "time":final_time}

    return data;

@app.get("/ow-west")
def ow_west():
    cursor = conn.cursor()
    resp = cursor.execute(f"""SELECT latency FROM "latencies" WHERE "server_name" = 'ow-west'""");
    print(resp)
    latency = cursor.fetchall()

    final_latency = []

    for x in latency:
        final_latency.append(x[0])

    resp = cursor.execute(f"""SELECT time FROM "latencies" WHERE "server_name" = 'ow-west'""");
    time = cursor.fetchall()

    final_time = []

    for x in time:
        final_time.append(x[0])

    data = {"latency":final_latency,
            "time":final_time}

    return data;


@app.get("/test")
def test():
    resp = {"list" : [1, 2, 3],
            "lists" : ["1", "2"],
            }
    return resp

# let's print CPU information
print("="*40, "CPU Info", "="*40)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")