from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
from bs4 import BeautifulSoup
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


url_to_all = "https://gpwbenchmark.pl/karta-indeksu?isin="

index_list = [
    "PL9999999987",
    "PL9999999375",
    "PL9999999912",
    "PL9999999979",
    "PL9999999995",
    "PL9999999482",
    "PL9999996439",
    "PL9999998377",
    "PL9999999565"
]

name_of_index = [
    "WIG20",
    "WIG30",
    "mWIG40",
    "sWIG80",
    "WIG",
    "WIGdiv",
    "WIGdivplus",
    "WIG140",
    "NCIndex"
]



@app.get("/orlen")
def orlen():
    url = "https://www.gpw.pl/spolka?isin=PLPKN0000018"
    
    
    return  getCompanyValue(url)

@app.get("/pzu")
def pzu():
    url = "https://www.gpw.pl/spolka?isin=PLPZU0000011"
    
    
    return  getCompanyValue(url)



@app.get("/pko")
def pko():
    url = "https://www.gpw.pl/spolka?isin=PLPKO0000016"
    
    
    return getCompanyValue(url)

@app.get("/all_index")
def all_index():
    response = []
    
    for i in range(len(index_list)):
        url = url_to_all + index_list[i]
        print(url)
        #row = [name_of_index[i],getIndexValue(url)]
        print(name_of_index[i]+"       "+  getIndexValue(url))
        response.append({
                "name": name_of_index[i],
                "Value": float( getIndexValue(url).replace(",", ".").replace('\xa0', ''))
            })

    return response
    



def getCompanyValue(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    value = float(soup.select_one(".summary").text.strip().replace(",", ".").replace('\xa0', ''))
    name  = soup.select_one("#getH1").text.strip()
    return {name: value }

def getIndexValue(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    value = soup.select_one(".summary").text.strip()
    #name = soup.select_one(".font30.font-light.padding-top-10.padding-bottom-5").text.strip()
    #return {name: value }
    return value

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )

