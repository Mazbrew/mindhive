from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.templatetags.static import static

import pandas as pd
import spacy
import json

# opening the csv and loading the model
df = pd.read_csv(static("dataset-preprocessed.csv")).set_index("Product ID")
nlp = spacy.load("en_core_web_md") 

# function to handle the post request
@api_view(['POST'])
def handleMessage(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    text = body['text']

    similarity_score, detected_category, items_kv = find_most_similar(df,text)

    return Response(create_response(similarity_score, detected_category, items_kv))

# finds the most relevant category in relation to the sentence
def find_most_similar(df, input):
    tokens = nlp(input)

    categories = pd.unique(df["Category"])

    max_similarity_score = 0.0
    similar_name = ""
    items_kv = []
    
    for token in tokens: 
        if(token.pos_ == "NOUN" or token.pos_ == "VERB"):
            for i in range(len(categories)):
                similarity_score = token.similarity(nlp(categories[i]))
                if(similarity_score > max_similarity_score):
                    max_similarity_score = similarity_score
                    similar_name = categories[i]

    if(similar_name != ""):
        items_kv = convert_to_key_value(df, similar_name)

    return max_similarity_score, similar_name, items_kv

# converts the dataframe in to key value pairs while also changing the name of the columns
def convert_to_key_value(df, category):
    items_df = df.loc[df["Category"] == category].rename(columns = {"Product Name":"product_name", "Description":"description", "Price":"price"})

    items_kv = items_df.to_dict('records')

    return items_kv

# returns the appropriate reply 
def create_response(similarity_score, detected_category, items_kv):
    if(similarity_score <= 0.2 and detected_category != ""):
        dict = {
            "text": "We do not have anything in the store that matches your criteria",
            "sender": "AI",
        }
    elif(detected_category == ""):
        dict = {
            "text": "I don't quite understand that",
            "sender": "AI"            
        }
    else:
        dict = {
            "text": "Here are some items that may be relevant to you:",
            "items": items_kv,
            "sender": "AI"
        }

    return dict