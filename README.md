# ServerSide-FinalProject

Trying to fix this :D

## Installation

First, download or clone the repo to a local folder :D
```
git clone https://github.com/willpaxton/ServerSide-FinalProject
```

### Windows 
Easiest way is to install docker desktop here: https://www.docker.com/products/docker-desktop/

Then, open a command line session within the project directory (aka the folder which contains the compose.yml file) and run 
```
docker compose up --build
```

### Linux
Same thing as above (with using Docker Desktop), or use docker CLI with the same command above to launch the project

Let Docker do its thing for a bit (could take up to 5 minutes to grab the images and set up the containers).

### Accessing

When running, go to http://localhost:3000/d/BwcXP3cnz/dashboard?orgId=1&refresh=5s&from=now-5m&to=now to pull up the dashboard
This adds autorefresh and sets a 5 minute data "history" for the latency charts.  This can be changed if desired.  This also may kick an error on the graphs, clicking on the "zoom to data" button will fix this :) 

Other endpoints
- API: Port 8080
- Adminer: Port 8081
- Grafana: Port 3000