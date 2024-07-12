import streamlit as st
import pickle
import requests

st.set_page_config(layout="wide")
movies=pickle.load(open('movies_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
st.header("Movie Recommendations")
movies_list=movies['title'].values
value=st.selectbox("Select the movies from Below",movies_list)


def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    dist=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    rec=[]
    for i in dist[1:6]:
        rec.append(movies.iloc[i[0]].title)
    return rec


if st.button("Show Reccommendations"):
    st.markdown("The best movies based on your search")
    movie_name=recommend(value)
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])