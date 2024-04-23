from pythonping import ping
import psycopg2
import time
from datetime import datetime, timezone
import asyncio


servers = {
    "ow-central" : "24.105.62.129",
    "ow-west" : "24.105.30.129",
    "val-na" : "192.207.0.1"
}

conn = psycopg2.connect(database="database",
                        host="db",
                        user="postgres",
                        password="password",
                        port="5432")

# conn.autocommit = True
# remember to commit silly :)
# also can manually commit by using conn.commit()

cursor = conn.cursor()

for key in servers:
    try: 
        print(cursor.execute("INSERT INTO servers (name, address) VALUES (%s, %s);", (key, servers[key])))
        conn.commit()
    except:
        print("This server already exists in the db... skipping...")
        conn.rollback()

print(cursor.execute("SELECT * FROM servers"))

def find_lat(ip_addr):
    lat = ping(ip_addr, verbose=True, count=10, size=8000)
    return lat.rtt_avg_ms

async def gather_lat():
    for key in servers:
        print(f"parsing {key}")
        latency = find_lat(servers[key])
        cursor.execute("INSERT INTO latencies (server_name, time, latency) VALUES (%s, %s, %s)", (key, datetime.now(timezone.utc), latency))
        conn.commit()
            
        
while True:
    asyncio.run(gather_lat())
    time.sleep(300)


