import requests
from bs4 import BeautifulSoup

url = 'https://api.csgorun.gg/current-state?montaznayaPena=null'

def getRunCfc():
  req = requests.get(url)
  inf = req.json()['data']['game']['history']
  
  cfc = []
  for item in inf:
    num = round(item['crash'], 2)
    
    def set_color():
      if num < 1.2:
        return '🔴'
      elif num < 2:
        return '🔵'
      elif num < 4:
        return '🟣'
      elif num < 8:
        return '🟢'
      elif num < 20:
        return '🟡'
      else:
        return '🔥'
    cfc.append(f'{set_color()} - | ```{str(num)}``` \n\n')
    
  return f'\n\n{"".join(cfc)}'