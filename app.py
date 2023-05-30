import streamlit as st
import pickle
import pandas as pd

df_original = pd.read_csv('all_drinks.csv')

def recommand(cocktail, number):
    input_cocktail = cocktail
    number = number + 1
    recommendations = pd.DataFrame(similarity.nlargest(number,input_cocktail)['strDrink'])
    recommendations = recommendations[recommendations['strDrink']!=input_cocktail]
    cocktailList = []
    cocktailThumbList = []
    for index, row in recommendations.iterrows():
        cocktailList.append(row['strDrink'])
        cocktailThumbList.append(df_original.at[index, "strDrinkThumb"])
    return cocktailList, cocktailThumbList
    

cocktails_dict = pickle.load(open('cocktail_dict.pkl', 'rb'))
cocktails = pd.DataFrame(cocktails_dict)

similarity = pickle.load(open('cocktail_similarity.pkl','rb'))

st.title('Cocktail Recommendation System')

selected_cocktail = st.selectbox('Choose the cocktail that appeals to you', cocktails['strDrink'].values)

df_original['strDrink'] = df_original['strDrink'].str.lower()
row = df_original.loc[df_original['strDrink'] == selected_cocktail]
strDrinkThumb = row["strDrinkThumb"].values[0] + '/preview'

st.header(selected_cocktail)
st.image(strDrinkThumb)

selected_number = st.slider('Choose how many you want the system to recommend', 1, 9, 3)

if st.button('Check out cocktails you might like'):
    cocktailList, cocktailThumbList = recommand(selected_cocktail, selected_number)

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)

    try:
        with col1:
            st.header(cocktailList[0])
            st.image(cocktailThumbList[0])
        with col2:
            st.header(cocktailList[1])
            st.image(cocktailThumbList[1])
        with col3:
            st.header(cocktailList[2])
            st.image(cocktailThumbList[2])
        with col4:
            st.header(cocktailList[3])
            st.image(cocktailThumbList[3])
        with col5:
            st.header(cocktailList[4])
            st.image(cocktailThumbList[4])
        with col6:
            st.header(cocktailList[5])
            st.image(cocktailThumbList[5])
        with col7:
            st.header(cocktailList[6])
            st.image(cocktailThumbList[6])
        with col8:
            st.header(cocktailList[7])
            st.image(cocktailThumbList[7])
        with col9:
            st.header(cocktailList[8])
            st.image(cocktailThumbList[8])
    except:
        pass
    