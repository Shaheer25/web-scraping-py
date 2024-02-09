from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()



TIMES_JOB = os.getenv("TIMES_JOB")
html_response = requests.get(url=TIMES_JOB).text

scarpe = BeautifulSoup(html_response,"lxml")

exp = scarpe.find_all('li',class_ = "clearfix job-bx wht-shd-bx" )

jobs=exp.find("h4",_class="joblist-comp-name").text

print(jobs)