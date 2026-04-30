import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()
df = df.dropna()

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['query'])

def get_response(user_query):
    user_vec = vectorizer.transform([user_query])

    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    score = similarity[0][index]

    # If no good match
    if score < 0.3:
        return {
            "law": "Not Found",
            "explanation": "Your query is unclear or not in our database.",
            "steps": "Please provide more details or try rephrasing."
        }

    result = df.iloc[index]

    return {
        "law": result['law'],
        "explanation": result['explanation'],
        "steps": result['steps']
    }
