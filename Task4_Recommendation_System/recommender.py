import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load data
movies = pd.read_csv("movies.csv")


# Fill missing values
movies["genres"] = movies["genres"].fillna("")


# Create clean movie names
movies["clean_title"] = (
    movies["title"]
    .str.replace(r"\s*\(\d{4}\)", "", regex=True)
)


# Convert genres into vectors
vectorizer = TfidfVectorizer(
    stop_words="english"
)

movie_vectors = vectorizer.fit_transform(
    movies["genres"]
)


# Similarity calculation
similarity = cosine_similarity(movie_vectors)



def recommend(movie_name):

    movie_name = movie_name.lower()


    # Search movie without year
    matches = movies[
        movies["clean_title"]
        .str.lower()
        .str.contains(movie_name)
    ]


    if len(matches) == 0:
        return []


    movie_index = matches.index[0]


    scores = list(
        enumerate(similarity[movie_index])
    )


    scores = sorted(
        scores,
        key=lambda x:x[1],
        reverse=True
    )


    recommendations = []


    for i in scores[1:6]:

        title = movies.iloc[i[0]]["clean_title"]

        recommendations.append(title)


    return recommendations