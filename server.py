from fastapi import FastAPI
import uvicorn
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DESC_URL = "https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json"
AVAIL_URL = "https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json"

@app.get("/api/parking")
def get_parking():
    desc = requests.get(DESC_URL, timeout=10).json()
    avail = requests.get(AVAIL_URL, timeout=10).json()
    return {"desc": desc.get("data", {}).get("park", []), "avail": avail.get("data", {}).get("park", [])}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)