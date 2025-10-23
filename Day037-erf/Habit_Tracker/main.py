import subprocess as sp; sp.call('cls', shell=True)
import requests, os

USERNAME = "erfawnhy"
TOKEN = os.environ.get("pixela_token")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
#Build a graph in api server
header = {
    "X-USER-TOKEN": TOKEN
}

# ##POST REQUEST TO MAKE A GRAPH
        # pixela_make_graph_params = {
        #     "id": "erfimerfi1",
        #     "name": "someTest",
        #     "unit": "death", 
        #     "type": "float",
        #     "color": "sora",
        # }
        # with requests.post( #POST Request to make a graph with 'someTest' name
        #     url= f"{PIXELA_ENDPOINT}/{USERNAME}/graphs",
        #     json= pixela_make_graph_params,
        #     headers=header) as rs:
        #     print(rs.text)


