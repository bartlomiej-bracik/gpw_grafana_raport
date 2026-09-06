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






@app.get("/orlen")
def orlen():
    url = "https://www.gpw.pl/spolka?isin=PLPKN0000018"
    
    
    return {"Notowania Orlen": getCompanyValue(url) }

@app.get("/pzu")
def pzu():
    url = "https://www.gpw.pl/spolka?isin=PLPZU0000011"
    
    
    return {"Notowania PZU": getCompanyValue(url) }



@app.get("/pko")
def pko():
    url = "https://www.gpw.pl/spolka?isin=PLPKO0000016"
    
    
    return {"Notowania PKO": getCompanyValue(url) }



def getCompanyValue(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    value = soup.select_one(".summary").text.strip()
    
    return value

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )

