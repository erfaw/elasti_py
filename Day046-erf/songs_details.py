import subprocess as sp; sp.call('cls', shell=True)
import requests as rq
## USE 'OFFICIALCHARTS' INSTEAD OF 'BILLBOARD' FOR GEO-BLOCKING
with rq.get("https://www.officialcharts.com/charts/singles-chart/20001022") as response:
    response.raise_for_status()
    print(response.text)