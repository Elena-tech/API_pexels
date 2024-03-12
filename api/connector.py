import os 
import requests
from dotenv import load_dotenv
from pexels_api import API

class pexel:
  def __init__(self):
    load_dotenv()
    self.apikey = os.getenv('API-KEY') #getting a key and printing it 
    #print(self.apikey)

  def search_api(self, search):
    api = API(self.apikey)
    # search five 'cats' photos
    api.search(search, page=1, results_per_page=5)
    # get photo entries
    photos = api.get_entries()
    return photos
