



from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json


url = "https://api.coingecko.com/api/v3/simple/price?x_cg_demo_api_key=https://api.coingecko.com/api/v3/coins/list"

headers = {"accept": "application/json"}

response = requests.get(url)

print(response.text)













