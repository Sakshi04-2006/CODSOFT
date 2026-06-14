import streamlit as st
from recommender import recommend


# Page settings

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎥",
    layout="centered"
)


# Styling

st.markdown(
"""
<style>

.main{
    background-color:#f5f7fb;
}


h1{
    text-align:center;
    color:#1f2937;
}


.subtitle{
    text-align:center;
    color:#6b7280;
    font-size:18px;
}


.card{

    background:white;
    padding:20px;
    border-radius:15px;
    margin:10px 0;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    background:#1f2937;
    color:white;

    font-size:18px;

}


</style>
""",
unsafe_allow_html=True
)



# Title

st.title(
    "AI Movie Recommendation System"
)


st.markdown(
"""
<p class="subtitle">
Machine Learning based movie suggestion system
</p>
""",
unsafe_allow_html=True
)


st.write("")


movie = st.text_input(
    "Enter movie name",
    placeholder="Example: Inception, 3 idiots, Avatar"
)



if st.button("Get Recommendations"):


    if movie.strip()=="":

        st.warning(
            "Please enter a movie name"
        )


    else:

        results = recommend(movie)


        if len(results)==0:

            st.error(
                "Movie not found. Try another movie."
            )


        else:

            st.subheader(
                "Recommended Movies"
            )


            for item in results:

                st.markdown(
                f"""
                <div class="card">
                {item}
                </div>
                """,
                unsafe_allow_html=True
                )



st.write("")
st.caption(
"Built using Python, Scikit-learn and Machine Learning"
)