!pip install bs4
!pip install requests


urlOverall = "https://www.maxpreps.com/in/basketball/rankings/1/"

urlClass = "https://www.maxpreps.com/in/basketball/23-24/{}/rankings/1/"

print(urlOverall)

import requests

control = requests.get(urlOverall)

for classDivision in classDivisions:
    
    urlClass = urlClass.format(classDivision)
    data = requests.get(urlClass)
    


with open("/IHSAA_Project/Rankings/{}.html".format("Overall"), "w+") as f:
    f.write(control.text)

from bs4 import BeautifulSoup
