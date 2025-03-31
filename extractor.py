import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def extract_info(text):
    doc = nlp(text)
    data = {"Invoice Number": None, "Date": None, "Amount": None}
    for ent in doc.ents:
        if ent.label_ == "MONEY":
            data["Amount"] = ent.text
        elif ent.label_ == "DATE":
            data["Date"] = ent.text
    return data

with open("sample_invoice.txt", "r") as f:
    text = f.read()
result = extract_info(text)
print(pd.DataFrame([result]))