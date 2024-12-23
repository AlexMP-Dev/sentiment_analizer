from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from pln import analisisSentiment, score

app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    data: List[List[str]]

@app.post("/analisis", status_code=200)
def create_item(item: Item):
    data = analisisSentiment(item.data)
    # Sumar las puntuaciones de todos los mensajes
    total_positive = sum([entry["positive"] for entry in data])
    total_negative = sum([entry["negative"] for entry in data])
    total_neutral = sum([entry["neutral"] for entry in data])

    overall_score = score(total_positive, total_negative, total_neutral)

    return {
        "processed_data": data,
        "overall_score": overall_score,
        "totals": {
            "positive": total_positive,
            "negative": total_negative,
            "neutral": total_neutral
        }
    }

