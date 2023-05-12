import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import csv
from .models import Tag
tag_file = './staticfiles/tags.csv'


tag_df = pd.read_csv(tag_file)

tfidf= TfidfVectorizer(stop_words="english")
tag_df['content']= tag_df['content'].fillna("")

tfidf_matrix= tfidf.fit_transform(tag_df['content'])

cosine_similarity= linear_kernel(tfidf_matrix, tfidf_matrix)

indices= pd.Series(tag_df.index, index=tag_df['title']).drop_duplicates()

def get_recommendation(title, cosine_sim=cosine_similarity):
    idx= indices[title]
    sim_score= enumerate(cosine_sim[idx])
    sim_score= sorted(sim_score, key= lambda x:x[1], reverse=True)
    sim_score= sim_score[1]
    sim_index = sim_score[0]
    top_tag = tag_df['title'].iloc[sim_index]
    return top_tag