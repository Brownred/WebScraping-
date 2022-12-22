import requests
from bs4 import BeautifulSoup

url = 'https://httpbin.org/get'
payload = {'key1':'value1','key2':'value2','key3':'value3'}

try:
    # try to get to a webpage
    # create a response object called r from where we can get all info we need
    r = requests.get(url,params=payload,timeout=0.001)
    
    # raise HTTP error for bad response code eg 4xx or 5xx
    r.raise_for_status()

# Handle Connection Timeout Errro 
except requests.exceptions.ConnectTimeout:
    print(f"Connection to {r.url} timed out. Try rerunning the script again or check your internet connection.")

# Handle Connection Error/DNS Failure
except requests.exceptions.ConnectionError:
    print("Check Your Internet Connection! Failed to establish a new connection.")
    
# Handle errors for bad response status code
except requests.exceptions.HTTPError:
    print(r.status_code)
    
else:
    print(f"Succesfully accessed {r.url}")
