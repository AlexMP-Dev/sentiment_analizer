
from typing import List
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# data = [
#     ["20/11/2024", "10:15 a. m.", "Juan Perez", "Las instalaciones están en muy mal estado, deberían invertir más en mantenimiento."],
#     ["20/11/2024", "11:00 a. m.", "Ana Lopez", "Los profesores no están capacitados, el nivel educativo es muy bajo."],
#     ["20/11/2024", "2:45 p. m.", "Carlos Gomez", "El horario es terrible, no consideran las necesidades de los alumnos."],
#     ["20/11/2024", "3:30 p. m.", "Laura Martinez", "No cumplen con lo que prometieron al inscribirnos, me siento decepcionada."],
#     ["20/11/2024", "4:20 p. m.", "Diego Ramirez", "Las clases están desorganizadas, no hay un plan de estudios claro."],
#     ["20/11/2024", "5:50 p. m.", "Sofia Alvarez", "Es inaceptable que haya tantos problemas técnicos en las aulas virtuales."],
#     ["20/11/2024", "6:10 p. m.", "Fernando Torres", "El personal administrativo nunca responde a las consultas, es frustrante."],
#     ["20/11/2024", "8:45 p. m.", "Mariana Sanchez", "El costo de la matrícula no vale la pena para la calidad que ofrecen."],
#     ["20/11/2024", "9:15 p. m.", "Luis Herrera", "Hay demasiada burocracia para resolver cualquier problema, no recomiendo este lugar."],
#     ["20/11/2024", "10:00 p. m.", "Carla Medina", "Las aulas están sucias y el ambiente no es adecuado para estudiar."]
# ]

def analisisSentiment(data: List[List[str]]):
    df = pd.DataFrame(data, columns=["Date", "Time", "contact", "Message"])
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    sentiments = SentimentIntensityAnalyzer()
    df["positive"] = [sentiments.polarity_scores(i)["pos"] for i in df["Message"]]
    df["negative"] = [sentiments.polarity_scores(i)["neg"] for i in df["Message"]]
    df["neutral"] = [sentiments.polarity_scores(i)["neu"] for i in df["Message"]]

    return df.to_dict(orient="records")


#data.head()

#x=sum(data["positive"])
#y=sum(data["negative"])
#z=sum(data["neutral"])

def score(a, b, c):
    if (a > b) and (a > c):
        return "Positive"
    if (b > a) and (b > c):
        return "Negative"
    if (c > a) and (c > b):
        return "Neutral"

#score(x,y,z)