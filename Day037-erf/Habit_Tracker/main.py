import subprocess as sp; sp.call('cls', shell=True)
import requests, os, datetime as dt

USERNAME = "erfawnhy"
TOKEN = os.environ.get("pixela_token")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_ENDPOINT_USER = f"{PIXELA_ENDPOINT}/{USERNAME}"
GRAPH_ID = "erfimerfi1"
current_day :str = (dt.date.today() - dt.timedelta(days=6) ).strftime(r"%Y%m%d")
#Build a graph in api server
header = {
    "X-USER-TOKEN": TOKEN
}
# ##POST REQUEST TO MAKE A GRAPH
        # pixela_make_graph_params = {
        #     "id": GRAPH_ID,
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

##POST A PIXEL TO GRAPH
pixela_post_pixel_params = {
    "date": current_day,
    "quantity": "10",
    # "optionalData": "this is a test optional data on someTest graph"
}
with requests.post(
    url= f"{PIXELA_ENDPOINT_USER}/graphs/{GRAPH_ID}",
    headers=header,
    json= pixela_post_pixel_params,
    ) as res:
    print(res.text)

