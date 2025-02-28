import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

import uvicorn

from pln import analisisSentiment, score

app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    data: List[List[str]]

@app.post("/analisis", status_code=200)
def create_item(item: Item):
    data = analisisSentiment(item.data)
    #Sumar las puntuaciones de todos los mensajes
    # total_positive = sum([entry["positive"] for entry in data])
    # total_negative = sum([entry["negative"] for entry in data])
    # total_neutral = sum([entry["neutral"] for entry in data])

    # overall_score = score(total_positive, total_negative, total_neutral)

    return {
        "processed_data": data,
        "overall_score": 0,
        "totals": {
            "positive": 0,
            "negative": 0,
            "neutral": 0
        }
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
